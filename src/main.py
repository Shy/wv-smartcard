#!/usr/bin/env python

import time
import subprocess
import process


def main():

    while True:
        # Run one process loop
        process.main()
        # Sleep to avoid 100% CPU usage
        time.sleep(5)


def clear_wifi(ch, evt):
    # When the button is pressed resin-wifi-connect is started with `--clear'
    # flag set to 'true'. This forces resin-wifi-connect to remove any
    # previously configured WiFi connections.2
    print("Button pressed")
    subprocess.call(["resin-wifi-connect", "--clear=true"])


if __name__ == "__main__":
    main()
