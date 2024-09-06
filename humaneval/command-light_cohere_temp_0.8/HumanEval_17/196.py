```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1}
    beat_counts = {'.':': 4, 'o' : 4, 'o|' : 2}

    def get_beat_count(note):
        return beat_counts.get(note, 0)

    notes_info = {note: [get_beat_count(note)] for note in notes}

    return list(notes_info.parse_music(music_string))

def test_parse_music():
    music_str = "o o| .| o| .| .| .| .| o o"
    notes = parse_music(music_str)

    print(notes == [4, 2, 1, 2, 2, 1, 1, 1, 4, 4])
``` 
This script defines a function **`parse_music`** that parses a music string, represented in a specific format, into a list of beat counts. The function utilizes a legend for the notes, mapping each character with its beat count associated with it. The **`test_parse_music`** function verifies that the **`parse_music`** function correctly returns the expected beat count for a given music string.