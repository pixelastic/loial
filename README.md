# loial

- Shutdown: ssh, then `sudo su -`, then `shutdown`

Branché, mais rien sur l'écran au boot
ls /dev/spi* donne rien. SPI semble protocole pour communique, might need to
activate it manually.

Install gpio
sudo apt update
sudo apt install raspi-gpio
déjà là, pourtant `gpio` was not found

`sudo raspi-config` => Interface options => Enable SPI

sudo reboot
didn't change anything, still no /dev/spi*

I'm installing neovim to edit the files
I updated /boot/firmware/config.txt to uncomment the dtparam=spi=on line
and rebooted
Now I have some /dev/spidev0.0 and /dev/spidev0.1

Now I:
`sudo apt install python3-pip`
<!-- `sudo apt install python3-pil` -->
<!-- `sudo apt install python3-numpy` -->

I also `git clone https://github.com/waveshare/e-Paper`
It should contain examples

It went to the example directory and ran `python3 epd_7in5_V2_test.py` and it
worked

Now, I have a base, I can start coding.
