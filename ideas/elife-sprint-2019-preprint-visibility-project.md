
# eLife Sprint working doc project pitch for sprint docs

Status: draft
Contributors: Naomi, ...

**Contributed by:** Naomi Penfold & Daniela Saderi
Problem statement: As a reader (and commenter/reviewer/PreLighter) of preprints, I would like to find preprints by authors with typically low visibility who are preprinting for the first time in order to prioritise reading & providing feedback on their preprints (and intentionally contribute to making preprints a success for everyone). This needs to be easy for me: I am motivated to counteract attention bias but I have little time to spend finding such preprints, I need to spend any time I have on the reading & writing about them.
**One-liner:** a prototype tool based on opinionated rules that filters a feed of the latest preprints for indicators of lower visibility of the author (first author?), such as:
* gender {female, see [sbotlite](https://sbotlite.github.io/) for how they estimate gender}
* geography {institutional affiliation, country -- e.g. countries with low [passport index](https://www.passportindex.org/byRank.php) for whom attending international conferences may be more difficult}
* twitter reach [follower count of authors]
* first-time preprinter [first author name&affiliation / ORCID doesn't match pre-existing preprints])
* ethnicity -- I think this would not be possible
The prototype should pick 1-2 simple rules only and may be restricted to a specific server (or set of servers) for which a feed is available and the metadata is sufficient to filter for preprints according to the rule above.
**Links/notes:** This project has a github repo at ..., containing further background information to this idea and our expectations for where it might go next.
Resources that may be helpful: biorxiv metadata dump (retrievable from rxivist data: ?), or eupmc data access.
**Call for contributors:** Are there particular skills that the project needs? (1) Developer(s)/data scientist(s) to write script to apply rule to a dataset of preprints and produce a tool that displays the filtered or marked output. Interoperability with existing preprint server(s) and third-party preprint commentary initiatives (PreLights, PreLists, PREreview, etc would be helpful); (2) Users: researchers, preprint commentary initiative leads & contributors; (3) Scientometrics/ethics specialist: how to create these filtering rules? How to be transparent?; (4) Someone(s) who would be interested to take project forward if prototype/idea is useful; (5) Someone who can design a nice web presence for the tool
**Interested contributors:** please list yourself here if you are interested in contributing to this idea at the Sprint.
