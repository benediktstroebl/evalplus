```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '|': 1}
    beats = music_string.replace(notes). ...
    : List[int
    beats.to_note_length = [0]
    for note in beats:
        for beat in range(beat, len(beats) - beat):
            if beats[beat:].isalpha(*note):
                to_note_length[note] += 1
            else:
                break
    return to_note_length

# Test cases
music_str = """
o o o| .| o| .| .| .| o o
o o| .| o| .| .| .| o o
"""

test_music = parse_music(music_str)
print(test_music == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4])  # Should print True
```
This function parse_music takes a string in a specific format representing musical notes and returns a list of integers corresponding to the number of beats for each note. The function uses a legend provided to interpret the format. Then, it creates a dictionary to map musical note characters to the number of beats each note lasts. Finally, it loops through the beats and checks if each beat is a valid combination of note characters. If it is, we increment the counter for that note. The function then returns the number of beats for each note.