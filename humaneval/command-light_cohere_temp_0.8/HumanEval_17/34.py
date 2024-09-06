```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        "o": 4,
        "o|": 2,
        ".":": 1,
        ".":": 4,
        ".":|": 4,
        "..": 4,
        "[]": 4,
        "{}": 2,
        "|.":": 1,
        "()": 2,
    }
    
    beat_counts = {note: value for note, value in notes. word beats} whole notes, each beat is four beats,
        a half note is half the length of a whole note,
        a quarter note is one-quarter the length of a whole note.

notes_str = music_string.split()
beat_counts_str = "\n".join: "o".join.pound: "o|".join: "",).  #".join(beat_counts_str.split())
beats = [0]

for note, beat_count in notes_str:
    beats[beat_count] += 1
beat_counts[note] = beats[beat_count]

beat_counts_str = "\n".join:", "\t".join: beat_counts_str

print(beat_counts)
``` 
This script defines a function called `parse_music` that takes a string of music notes and returns a list of integers corresponding to the number of beats in each note. It uses a legend of notes and their beats to map the notes to the corresponding beat counts, and then uses a loop to iterate through the notes in the music string, incrementing the beat count for each note.  The output of the beat count will be a string formatted as needed for the test.