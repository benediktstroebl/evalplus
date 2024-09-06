Here is a self-contained Python script that implements the `parse_music` function from the previous prompt:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    def parse(note):
        if note == 'o': return 4
        elif note == 'o|': return 2
        elif note == '.|': return 1
        else: raise ValueError("Invalid note format")
    
    notes = music_string.split(' ' ')
   
    notes = [note for note in notes if note.contains('.')]
    whole_note = len(notes) % 4
    notes = [parse(note) for note in notes if note not in ['o', 'o|', '.|']]
    
    return notes

# Test cases
test_cases = [
    "o o| .| o| .| .| .| o o",
    ".", ".", ".", ".", ".|.", ".|.", ".", "o o",
    ".", ".", ".o|.", "o|o",
    "o o o",
    "|".", o|.", ".o|.", ".o|o",
    ".o o|.", ".", ".o|.", "o|o|.", "|o|.",
]

for test_case, expected_notes in zip(test_cases, parse_music(test_case)):
    print(f"Expected: {`, expected_notes, f"} Got: {", [len(note) for note in expected_notes], f"}")
```
This code defines a function `parse_music` that takes a music string in a special format, then splits the string into individual notes and their durations. The `parse` function uses a recursive approach to parse the music string. The function then returns a expected list of integers, corresponding to how many beats each note lasts.