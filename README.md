# loial

## First boot

First time I booted the Raspberry Pi Zero, I had to do some configuration to get
the screen to work. Namely:

- `sudo apt install neovim`
- `sudo nvim -p /boot/firmware/config.txt` and uncomment the `dtparam=spi=on`
line
- `sudo apt install python3-pip`
- `reboot`

I also cloned `https://github.com/waveshare/e-Paper` and tested the examples
(`python3 epd_7in5_V2_test.py` was the correct one)
