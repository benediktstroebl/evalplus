Here's a self-contained Python script that implements the `parse_music` function from the previous prompt:

```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format
    - Returns list of integers corresponding to how many beats does each last note last
    """
    notes = {'o': 4, 'o|': 2, '.|': 1}
    beats = [notes[ch] for ch in music_string.get(0, 'o')]
    return beats
```

This function takes a string music_string in a format like the one in the previous problem, and then uses a dictionary `notes` to map the ASCII characters to the number of beats they correspond to, then iterates over each character in the music string and adds the number of beats that the character correpond to a list called beats. 
Finally, the function returns this list of beats.