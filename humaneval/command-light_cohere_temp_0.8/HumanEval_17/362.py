Below is a Python script that defines a self-contained function, `parse_music`, which takes a string representing music notes in a special ASCII format and returns a list of integers representing the duration of each note in beats.
```python
def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1,
        others: []
    }
    result = []
    current_beat = 0
    for note in music_string:
        if note in notes:
            result.append(current_beat)
            current_beat += notes[note]
        else:
            result.append(current_beat)
            current_beat = 0
    return result
```