```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    """
    Parses a string representing musical notes in a special ASCII format.
    Format: 'o' - whole note, lasts four beats
    'o/' - half note, lasts two beats
    './' - quater note, lasts one beat
    Returns: list of integers, where each integer represents how many beats does each note last.
    Test cases:
    'o o| .| .
    'o o| .| .| .| .| o o'
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    beats = {'.': : 4, 'o/': 2, '.' : 1}
    
    pattern = r'(?P<([oOoO]|.).*)(? Somthing)'
    pattern = re.P converts to any 'o pattern', so we can match every part of the music.
 music_string: "o o| .| .| .| .| .| .| o o"
beats: {'.': : 4, 'o/': 2, '.' : 1}
notes = pattern.split()
 notes
counts = map(beats.get, notes)
return map(notes, counts)
```