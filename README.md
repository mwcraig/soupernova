# soupernova

[![PyPI - Version](https://img.shields.io/pypi/v/soupernova.svg)](https://pypi.org/project/soupernova)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/soupernova.svg)](https://pypi.org/project/soupernova)

-----

## Table of Contents

- [Installation](#installation)
- [Motivation](#motivation)
- [Usage](#usage)
- [License](#license)

## Installation

```console
pip install soupernova
```

## Motivation

Who wouldn't want this:

![Stars with confetti stars exploding from them](https://github.com/user-attachments/assets/884e42f6-0868-48e9-abd1-74998ae3e5de)

## Usage

If you happen not to have any astronomical images lying around you can just do this in a Jupyter notebook:

```python
from soupernova import SouperNova
sn = SouperNova()
sn
```

Once you see an image on the screen, click on it!

If you have a FITS image you can pass it in like this:

```python
from soupernova import SouperNova
sn = SouperNova(file="path/to/your/image.fits")
sn
```

## License

`soupernova` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
