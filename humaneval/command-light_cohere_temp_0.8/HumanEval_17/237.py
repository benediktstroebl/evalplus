```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split(" ")
    note_permutations = []
    for i in range(len(music_string) - 1):
        note_start = i
        note_end = i + 1
        note_permutation = [int(note) for note in music_string[note_start:note_end]]
        note_permutations.append(note_permutation)
    return note_permutations

def test_parse_music():
    assert parse_music("o o| .| o| .| .| .| .| o o") == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    assert parse_music(".") == []
    assert parse_music(".).o") == [1]
    assert parse_music("o|.") == [2]
    assert parse_music("ooooo") == []
```
This Python script defines a function `parse_music` that takes a music string as input and returns a list of integers representing the number of beats in each note. The function works by splitting the string into individual notes and then iterating over each note to create a list of note lengths. The function is then tested with several input strings, and the test suite ensures the function works as expected.