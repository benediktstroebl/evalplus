Here is a self-contained Python function that solves the problem of parsing markdown music notation into a list of integers representing the duration of each note in beats:
```python
from typing import List
from collections import defaultdict

NOTES = {'.o': 'whole', 'half', 'quarter'}

def parse_music(music_string: str) -> List[int]:
    notes = defaultdict(List)
    for note in NOTES:
        beat_count = [0] * 4
        for beat in range(4):
            if note == '.' and music_string[len(music_string) - beat - 1: -1] == '|':
                break
            else:
                beat_count[beat] += 1
                notes[note].append(beat_count)
        return notes
```
This function takes a string music_string as input and returns a list of integers. It uses a this defaultdict to efficiently store the duration of each note, and a list to keep track of whole, half, and quarter notes. The function iterates through the string, and adds up the beats for each note to get the total duration. It also adds the might beat count to the appropriate list for the corresponding note. 

Note that the function assumes the input is in the format of markdown music notation, with each note separated by a vertical bar (|). This is a common and simple format, but feel free to modify the function to match your specific requirements.