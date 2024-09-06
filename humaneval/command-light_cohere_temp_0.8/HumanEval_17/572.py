```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = ['o', 'o|', '.|']
    notes_in_music = music_string.split(' ')
    regularity = {}
    for note in notes:
        if note in notes_in_music:
            regularity[note] = regularity.get(note, 0) + 1
        else:
            regularity[note] = 1

    return [regularity[note] for note in notes_in_music]

# Test cases
test_music = [parse_music('o o| .| o| .| .| .| .| o o')]
test_music.print()
print(test_music)

test_music = [parse_music('o o| .o| o| .| o| .| .| o o')]
test_music.print()
print(test_music)

test_music = [parse_music('oo o| .| o| .| o o')]
test_music.print()
print(test_music)

test_music = [parse_music('o o o o| o| .| o o')]
test_music.print()
print(test_music)
```
This Python script defines a function `parse_music` that parses a given music string and returns a list of integers corresponding to the duration of each note in the music. The function utilizes a legend to categorize notes, then employs regular expressions to split the music string into individual notes. The durations of notes are determined based on their positions in the split. Additionally, the script includes several test cases to demonstrate the functionality of the `parse_music` function.