```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.|' : 1}
    
    pattern = '([{0}]) ([{1}]) ([{2}])'
    matches = re.sub(pattern, music_string, r'\3\1\2', \
                lambda m: int(m.group(0)) in notes and int(m.group(1)) in notes and int(m.group(2)) in notes)
    return matches
``` 
This Python function `parse_music` reads in a string of music notes represented in a special ASCII format, and returns a list of integers corresponding to how many beats each note lasted. The function uses regular expressions, and a substitiation function to match the input music string to a pattern that identifies the different note lengths. 

Please note that this solution uses the regex backtracking approach which can be computationally expensive for long strings and is not the most efficient solution. The function also uses string grouping to reduce the number of possible combinations which significantly improves its performance.