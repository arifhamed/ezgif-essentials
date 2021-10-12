# ezgif-essentials
Want to generate GIFs of the highest quality? Tired of having too many unecessary parameters? You also happen to be a motion graphic designer? `ezgif-essentials` is a pseudo-opinionated video/sequence to GIF CLI converter. It uses the same robust conversion pipeline as [ezGIF](https://ezgif.com/) without the frame rate limitations or involuntary compression. It is powered by [FFmpeg](https://github.com/kkroening/ffmpeg-python), [Gifsicle](https://github.com/kohler/gifsicle) and my frustration with all GIF converters.

|Converted by ezgif-essentials                    |Converted by ezgif.com                    |
|-------------------------------------------------|------------------------------------------|
|![](resources/converted-by-ezgif-essentials.gif) | ![](resources/converted-by-ezgif.com.gif)|

> Comparisons are both generated with their highest respective settings. There isn't even a competition. The answer is obvious.

## Installation
```bash
$ git clone https://github.com/winstxnhdw/ezgif-essentials.git
$ pip install -r requirements.txt
$ sudo apt install gifsicle
$ python main.py -h
```

## Usage (Video)
> Transparency is disabled by default to allow for more colour palettes when generating more complex GIFs 

```bash
$ python main.py -i test.mp4 -z 3
```

```yaml
Optional arguments:
-h, --help              show this help message and exit
-z, --optimise          optimise GIF file size with zero quality penalty
-l, --lossy             applies compression by allowing some artefacts
-w, --transparent       enables transparency
```

## Usage (Sequence)
> WARNING: Please name your images with the appropriate amount of leading zeros. Read more about it [here](https://unix.stackexchange.com/questions/77016/ffmpeg-pattern-type-glob-not-loading-files-in-correct-order).

```bash
$ python main.py -i 'image/*.png' -a -r 50 -z 3
```

```yaml
Required arguments:
-a, --assemble          prepares the script for an image sequence

Optional arguments:
-h, --help              show this help message and exit
-r, --fps               set the fps of the resultant GIF
-z, --optimise          optimise GIF file size with zero quality penalty
-l, --lossy             applies compression by allowing some artefacts
-w, --transparent       enables transparency
```
