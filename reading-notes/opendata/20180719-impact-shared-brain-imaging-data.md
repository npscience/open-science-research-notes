# :warning: LICENSE NOTE :warning:
The contents of this file is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), with attribution required to Naomi Penfold for free text, and to the authors of the manuscript as listed below for quoted text. This license note supersedes the general license in this repo. This is to match the license applied to the original research work, given my notes are very close to their text and include direct quotes.

# Source details
Title: Assessment of the impact of shared brain imaging data on the scientific literature
Authors: Michael P. Milham(corresponding), R. Cameron Craddock, Jake J. Son, Michael Fleischmann, Jon Clucas, Helen Xu, Bonhwang Koo, Anirudh Krishnakumar, Bharat B. Biswal, F. Xavier Castellanos, Stan Colcombe, Adriana Di Martino, Xi-Nian Zuo & Arno Klein
Source DOI: https://doi.org/10.1038/s41467-018-04976-1 (OA)
Resources: Code and data available at https://github.com/ChildMindInstitute/Biblio_Reader/blob/165ddc56779a5e55149184a0f95b7c14874cf0c5/biblio_reader/text_tools/text_tools.py

# Notes
The authors analysed publications arising from open neuroimaging data, a case study of the datasets in the International Neuroimaging Data-sharing Initiative (INDI): "FCP, NKI-RS, ADHD-200, ABIDE, and CoRR", to assess benefit of these open data projects.

Of 913 publications found from 2010-2017:
* Published by authors who were affiliated with institutions around the world (50 countries, 6 continents), but ~50% US. 90% of publications were authored by teams that did not include any data contributors, i.e. reuse by independent labs. For NKI-RS specifically, where the project is specifically designed to create data for others to use, 189 publications have been published so far, of which majority (167) do not include the NKI-RS PIs as authors and a substantial proportion (76; 40%) are by authors with no relationship to the project PIs. **Projects funded to create open data for others lead to knowledge creation by others**
* Publication type: 80% were peer-reviewed journals; rest were majority preprints and theses.
* Impact on literature: publications had been cited on average 4.4 times per year, total nearly 21,000 times.
* Publication destination: Of the journals, half were specific to neuroscience and related areas. So half the publications were in subject-specific journals. Judged journal impact using CiteScore; 25% pubs were in journals with CiteScore of 6.71 or higher. Two of the three top destinations (by amount of publications) were also high-ranking field-specific brain imaging journals: NeuroImage and Human Brain Mapping, therefore publications of secondary data analysis of open datasets do get into high impact field-specific journals.
* Compared publication destination to:
  * closed data - 50 ABIDE papers compared to 1834 papers matched to field (MRI studies of autism) and found similar cumulative density curves of % publications v CiteScore, indicating similar impact publication destinations
  * other data-sharing initiatives - looked at 175 publications from Human Connectome Project data - similar curves
  * general literature - 4000 papers on Web of Science with "MRI" and "brain" keywords in same timespan as searched for with INDI papers (2010-2017) -> also similar curve but slightly lower than HCP and INDI, where these have more publications in higher impact journals
  Overall, publications that are analyses of open datasets do not fare worse than general literature or closed data analyses. **For neuroimaging, it is not a drawback to conduct a secondary data analysis without any new data of your own.**

**Code is also reused** A further 71 publications did not use NDI data but reused the scripts/code shared by the INDI projects.

**Further data sharing follows** Several derivative projects sharing preprocessed data: "the Preprocessed Connectomes Project (http://preprocessed-connectomes-project.org), the R-fMRI Maps Projects (http://mrirc.psych.ac.cn/RfMRIMaps), and the C3-Brain Project (http://mrirc.psych.ac.cn/3C-BrainProject)"

**$1bn saved so far** The authors estimate that the INDI data sharing efforts have save between $900m and $1.7bn.
