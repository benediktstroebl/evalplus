```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = ['o', 'o', '|', 'o', '.', 'o', '.', '|', 'o', '.']
    beats = [1, 2, 4, 1, 2, 4, 2, 4, 2, 4]

    def parse(note):
        if note in notes:
            return beats[notes.index(note)]
        else:
            raise ValueError(f"Invalid note: {note}")

    return parse('o o| .| o| .| .| .| .| o o')

# Test cases
music_cases = [
    "o o| .",
    "x",
    ".",
    "o|.",
    "oo",
    "|.",
    "oo|.",
    "oo o",
    "|ooo",
]

correct_output = []

for music_case in music_cases:
    actual_output = parse_music(music_case)
    assert actual_output == correct_output, f"Failed in test case: {music_case}"

print(f"All tests passed.")
``` 
The code defines a function called `parse_music` that takes a music string as input and returns a list of integers. The integers represent the process the notes in the music and the number of beats they last. The code also provides several test cases to validate the correctness of the function.