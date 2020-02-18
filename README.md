# APAC

Automatic parcellation of auditory cortex (APAC)

APAC is a lightweight module for parcellate human brain auditory cortex. It is primarily intended for dividing the auditory cortex into subregions.

The current version of APAC requires preprocessed T1- and T2-weighted MRI data according to the [HCP pipelines](https://github.com/Washington-University/HCPpipelines). Essentially, MyelinMaps and Curvature data are required.

## Code

Install APAC with:

`pip install apac`
 
 Usage:

Here is an example script.
```python
import apac
path_out = '/path/folder/for/output/core'
fs_path = '/freesurfer/output/path'
hemi = 'L' # direction of hemisphere ['L' or 'R'] 

# initialize core processor
ppcore = apac.core.core(path_out)

# load freesurfer output path ("fsaveage_LR32k") 
ppcore.call(fs_path)  

# define initial ROI using HCP-MMP atlas
ppcore.initial_roi(hemi)

# define ppcore
ppcore.def_ppcore(hemi)
```
 

## License

- APAC is licensed under the terms of the MIT license.

## Conference

- 'Fully automated parcellation of the primary auditory cortex', SfN 2019 [Link](https://www.abstractsonline.com/pp8/#!/7883/presentation/50268)


## Core development team

- Sean H. Lee - Max Planck Institute for empirical aesthetic
- Bo-yong Park, MICA Lab - Montreal Neurological Institute
- Kyoungseob Byeon, MIPL - Sunkyunkwan University
