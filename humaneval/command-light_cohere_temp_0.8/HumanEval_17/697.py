Here's a self-contained Python script with a function that parses markdown music code and returns a list of note durations:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Input to this function is a string representing musical notes in a special ASCII format.
    Your task is legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    Return:
    list of integers corresponding to how many beats does each note last
    """
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    
    beats = {
        'o': 4,
        'o|': 2,
        '|': 1
    }
    
    notes_list = List(notes.items())
    beats_list = List(beats.items())
    
    music_notes = music_string.split(' ' ')
    split_notes = [note.split(' / '|') for note in music_notes]
    
    result = []
    for note_duration, beat_duration in zip(note_duration, beat_notes):
        result.append(beat_duration[0] * notes_list[note_duration])
    
    return result
``` 
This function takes a string of music notes in a special ASCII format and returns a list of integers representing the duration of each note in beats.