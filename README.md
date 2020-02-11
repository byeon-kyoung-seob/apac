# APAC

Automatic parcellation of auditory cortex (APAC)

APAC is a lightweight module for parcellate human brain auditory cortex. It is primarily intended for dividing the auditory cortex into subregions.	

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

ppcore = apac.core.core(path_out)
ppcore.call(fs_path)
ppcore.initial_roi(hemi)
ppcore.def_ppcore(hemi)
```
 

## License

-

## Support

*

## Paper

*
## Core development team

- Sean H. Lee - Max Planck Institute for empirical aesthetic
- Bo-yong Park, MICA Lab - Montreal Neurological Institute
- Kyoungseob Byeon, MIPL - Sunkyunkwan University
"# apac" 
