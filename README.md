# When The Sun Goes Down

## Requirements

* [solunar](https://github.com/kevinboone/solunar_cmdline)
* [whereami](https://github.com/slozo/WhereAmI) ⚠️  Manual installation (xcode needed)

## Installation

Clone the repo

`$ git clone git@github.com:welcoMattic/whenTheSunGoesDown.git`

Add a crontab job

`$ crontab -e`

Write this line

```crontab
/15 * * * * /path/to/whenTheSunGoesDown.py
```

Change the paths to day/night wallpapers in Python script

Enjoy ☀️  🌙

## Credits

* [Carlos Evo](https://github.com/CarlosEvo) for the [initial idea](https://www.reddit.com/r/unixporn/comments/76a1xr/macos_auto_darkmode_with_control_plane/) posted on Reddit
* [Mathieu Santostefano](https://github.com/welcomattic/) for this full python adaptation
* [All contributors](https://github.com/jolicode/deploylib/graphs/contributors)


## License

whenTheSunGoesDown is licensed under the [WTFPL License](http://www.wtfpl.net/about)

![WTFPL](http://www.wtfpl.net/wp-content/uploads/2012/12/freedom.jpeg)
