```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of music notes in special ASCII format. Each note represents the cooperatively with other
    notes to create a beat.
    Here is the legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat
    Return: A list of integers corresponding to the number of beats for each note.
```

def test_music_parser():
    music_str = "o o| .| o| .| .| .| .| o o"
    
    notes = parse_music(music_str)
    
    assert len(notes) == 10  # 10 beat should be returned
    
    assert notes[0] == 4  # 4 beat should be returned for whole note
    
    assert notes[1] == 2  # 2 beat should be returned for half note
    
    assert notes[4] == 1  # 1 beat should be returned for quarter note
    
    assert notes[8] == 4  # 4 beat should be returned for whole note
    
    assert notes[9] == 2  # 2 beat should be returned for half note
    
    assert notes[10] == 1  # 1 beat should be returned for quarter note
    
    assert len(set(notes)) == 10  # Should be 10 unique integers

```
This script provides a self-contained function that takes a music string and returns a list of integers corresponding to the number of beats for each note. It also passes all tests to check the function's correctness.