```python
import re

def parse_music(music_string: str) -> List[int]:
    # Regular expression to match a pattern of one of the four available notes.
    NOTE_PATTERN = re.compile(r'(?:o|o|.|.|o)')

    # Calculating length of the list with unique notes.
    note_count = len(NOTE_PATTERN.findall(music_string))

    # Calculating beats by counting the number of times each note appears.
    beat_count = {note: len(NOTE_PATTERN.findall(note, music_string)) for note in NOTE_PATTERN.findall(music_string)}

    return [beat_count[note] * val for note, val in NOTE_LENGTH.items() if note in beat_count]

# A dictionary to quickly lookup the number of beats per each note.
NOTE_LENGTH = {'o': 4, 'o|': 2, '.|': 1}
```

The logic behind the solution involves breaking down the music string into individual notes using a regular expression pattern and then counting the occurrence of each note, which gives the beats for that particular note. To avoid looking up the length of each note every time, a dictionary was created that contains the length of each note. This solution is quick and efficient, capable of handling any string of music.