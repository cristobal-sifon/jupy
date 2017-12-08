# jupy
IPython default settings for jupyter notebook

## *Superseded by https://github.com/cristobal-sifon/ipystartup*

Clone this repository into somewhere convenient and `cd` into that directory. For me this might be something like

```
cd ~/git
git clone https://github.com/cristobal-sifon/jupy.git
cd jupy
```

Although there is no installation required, there is a `setup.py` file included. Execute this file to receive instructions on how to make this repository functional. Running `python setup.py` (no `install` option) will produce the following output:

```
No installation required. Please add the following line to your `~/.bashrc` 
or `~/.bash_profile`:

    export jupy=/path/to/jupy

or to your `~/.cshrc`, `~/.tcshrc`, etc:

    setenv jupy /path/to/jupy
```

where instead of `/path/to/jupy` you will see the actual location of the package. Follow those instructions and restart the console.

To load the settings provided here, type within an IPython notebook

```
import os
%run {os.environ['jupy']}/default.ipynb
```

(yes, with brackets and all.) By doing this, your notebook will:
  * Be compatible with both Python 2.x and 3.x;
  * have IPython pretty display loaded;
  * have the ability to show plots within the notebook;
  * have the following modules already loaded: 
    * `os`,
    * `numpy as np`,
    * `matplotlib.pyplot as plt`,
    * `sys`;
  * show plots with a nicer format (thicker axes, bigger labels, etc), if you have [`plottools`](https://github.com/cristobal-sifon/plottools) installed.
