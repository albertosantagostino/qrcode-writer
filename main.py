#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script to easily generate QR codes using existing libraries
"""

import getpass
import sys
import wifi_qrcode
import qrcode as qr

from simple_term_menu import TerminalMenu


def make_wifi_qrcode():
    ssid = input("Enter the SSID:\n")
    password = getpass.getpass("Enter the password:\n")

    qrcode = wifi_qrcode.make_wifi(ssid=ssid, auth=wifi_qrcode.utils.AuthType.WPA2, password=password)
    img = wifi_qrcode.utils.make_image(qrcode, wifi_qrcode.utils.ImageFormat.PNG)
    img.save(open('wifi_qrcode.png', 'wb'))

    print("WiFi QR Code created as wifi_qrcode.png")


def make_url_qrcode():
    url = input("Enter the URL:\n")

    qrcode = wifi_qrcode.make_link(url=url)
    img = wifi_qrcode.utils.make_image(qrcode, wifi_qrcode.utils.ImageFormat.PNG)
    img.save(open('url_qrcode.png', 'wb'))

    print("URL QR Code created as url_qrcode.png")


def make_text_qrcode():
    text = input("Enter the text:\n")

    qrcode = qr.make(text)
    qrcode.save(open('text_qrcode.png', 'wb'))

    print("URL QR Code created as text_qrcode.png")


if __name__ == '__main__':
    main_menu_title = "  QR Code creator\n"
    main_menu_items = ["WiFi QR Code", "URL QR Code", "Text QR Code", "Quit"]
    tm = TerminalMenu(menu_entries=main_menu_items, title=main_menu_title, cycle_cursor=True, clear_screen=True)
    sel = tm.show()

    if sel == 0:
        make_wifi_qrcode()
    elif sel == 1:
        make_url_qrcode()
    elif sel == 2:
        make_text_qrcode()
    elif sel == 3:
        sys.exit()
