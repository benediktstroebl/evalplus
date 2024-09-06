```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1}
    pattern = r'(\d+)'
    
    notes_in_pattern = re.sub(pattern, music_string, lambda m: [int(m.strip())])
    
    return [notes_in_pattern.to]
```
This Python code defines a function called `parse_music` that takes a music string in a specific format (a sequence of letters representing notes and rests) and returns a list of integers. The integers represent the number of beats that each note and rest would last, according to the provided legend. The code uses the legend, where 'o' represents a whole note that lasts four beats, 'o|' represents a half note that lasts two beats, and '.' represents a quarter note that lasts one beat. The code uses the particular format to the music string and uses the re-extraction technique to pull out the numbers of notes and rests. It utilizes a particular dictionary called notes to map the letters to the appropriate number of beats.