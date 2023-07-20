
GFPGAN aims at developing a Practical Algorithm for Real-world Face Restoration.

**Dependencies and Installation**

- Python >= 3.7 (Recommend to use [Anaconda](https://www.anaconda.com/download/#linux) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html))
- [PyTorch >= 1.7](https://pytorch.org/)
- Option: NVIDIA GPU + [CUDA](https://developer.nvidia.com/cuda-downloads)
- Option: Linux

# Install basicsr 
# We use BasicSR for both training and inference
pip install basicsr
# An open-source image and video restoration toolbox
# https://github.com/XPixelGroup/BasicSR 

# Install facexlib 
# We use face detection and face restoration helper in the facexlib package
pip install facexlib
# A collection that provides useful face-relation functions
# https://github.com/xinntao/facexlib 

# If you want to enhance the background (non-face) regions with Real-ESRGAN,
# you also need to install the realesrgan package
pip install realesrgan
# A practical algorithm for general image restoration
# https://github.com/xinntao/Real-ESRGAN 

pip install -r requirements.txt
python setup.py develop


**Inference!**

```bash
python quality_improvement.py -i data -o output -v 1.3 -s 2
```

```console
Usage: python quality_improvement.py -i inputs/whole_imgs -o output -v 1.3 -s 2 [options]...

  -h                   show this help
  -i input             Input image or folder. Default: data/input_sample.jpeg
  -o output            Output folder. Default: output
  -v version           GFPGAN model version. Option: 1 | 1.2 | 1.3. Default: 1.3
  -s upscale           The final upsampling scale of the image. Default: 2
  -bg_upsampler        background upsampler. Default: realesrgan
  -bg_tile             Tile size for background sampler, 0 for no tile during testing. Default: 400
  -suffix              Suffix of the restored faces
  -only_center_face    Only restore the center face
  -aligned             Input are aligned faces
  -ext                 Image extension. Options: auto | jpg | png, auto means using the same extension as inputs. Default: auto
```
