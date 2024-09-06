Here is a Python script that is fully self-contained with the function `parse_music()` which solves the problem according to the legend you provided:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    notes_nums = {note: notes[note] for note in music_string.print(notes_notes)
    return [notes_nums[note] for note in music_string.test_music(music_string)]

def test_music(music_string: str):
    notes = {'o': 4, 'o|': 2, '.|': 1}
    music_nums = parse_music(music_string)
    for note, beat in notes.
    assert beat == music_nums[note], f"Incorrect result for {note}, expected {beat} but got {music_nums[note]}."
    return music_nums
```

The code defines a function `parse_music` that takes a music string in a specific format (which is described in the previous response) and parses it into a list of integers representing the number of beats of each note. The `test_music` function is also provided, which takes a music string and expects the output of `parse_music`.  It then performs the same parsing operation and checks the results against the expected values from the `parse_music` function.