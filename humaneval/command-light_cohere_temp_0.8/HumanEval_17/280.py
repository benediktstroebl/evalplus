```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    
    beats = 0
    notes_found = {note: beats for note in notes. The music_string is split into notes using whitespace as separator and the beginning of each note is also mandatory.

    notes_found[music_string[0]] = beats
    for note in music_string[1:]:
        if note in notes_found:
            beats += notes_found[note]
        else:
            notes_found[note] = beats

    return beats

# Test cases
test_cases = [
    "o o| .| o| o| .| .| .| o o", [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4],
    "oo o o o o", [4, 4, 4],
    "o o o|.", [4, 2, 1],
    "o| o o", [1, 4],
    "|.o.", [1]
]

for case in test_cases:
    print(parse_music(case))
``` 
This function parse_music takes a string music_string representing notes in the same format. The music_string is split into notes and the function fills a dictionary with the notes and their beats. The function then loops through the notes and checks if the current note is already in the dictionary, if it is, it adds the beats to the corresponding key. If the note is not in the dictionary, it creates a key with the note and adds the beats to the corresponding key. The beats variable keeps track of the total beats, and it starts with zero. The function returns the final number of beats found.