```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = ['o', 'o','.|','.|']
    notes_map = {note: i for i, note in enumerate(notes)}
    
    def get_beat(note):
        if note == 'o':
            return 4
        elif note == 'o|':
            return 2
        elif note == '|':
            return 1
        else:
            raise ValueError("Invalid note")
    
    beats = [get_beat(note) for note in music_string.format_notes]
    
    return [beats]

# Test
parse_music('o o| .| o| .| .| .| .| o o')
 ```
The function parse_music takes a string music_string as input and uses a predefined set of notes and their corresponding beat values. The get_beat helper function is used to determine the beat value for each note. The main function creates a list of beats by iterating over the notes in the music_string. 

This function is self-contained and solves the problem of parsing a music note representation into a list of beat values.