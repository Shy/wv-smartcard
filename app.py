from time import sleep

from smartcard.CardMonitoring import CardMonitor, CardObserver
from smartcard.util import toHexString
import inky
from PIL import Image, ImageDraw,ImageOps
import qrcode

display = inky.auto()

qr = qrcode.QRCode(
    version=1,
    box_size=3,
    border=2,
)
qr.add_data('Some data')
qr.make(fit=True)

img = qr.make_image(fill_color=inky.BLACK, back_color=inky.WHITE)
print (display.resolution)
print(img.size)


img = ImageOps.expand(img,display.resolution,inky.WHITE)
print(img.size)
display.set_image(img)

display.show()

# a simple card observer that prints inserted/removed cards
class PrintObserver(CardObserver):
    """A simple card observer that is notified
    when cards are inserted/removed from the system and
    prints the list of cards
    """

    def update(self, observable, actions):
        (addedcards, removedcards) = actions
        for card in addedcards:
            print("+Inserted: ", toHexString(card.atr))
       
        for card in removedcards:
            print("-Removed: ", toHexString(card.atr))
         


if __name__ == "__main__":
    print("Insert or remove a smartcard in the system.")
    print("This program will exit in 10 seconds")
    print("")
    cardmonitor = CardMonitor()
    cardobserver = PrintObserver()
    cardmonitor.addObserver(cardobserver)

    sleep(10)

    # don't forget to remove observer, or the
    # monitor will poll forever...
    cardmonitor.deleteObserver(cardobserver)

    import sys

    if "win32" == sys.platform:
        print("press Enter to continue")
        sys.stdin.read(1)


