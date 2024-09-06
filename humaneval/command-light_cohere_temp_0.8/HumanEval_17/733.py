```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '|': 1}
    beat = 1

    notes = {key: notes[key] for key in music_string.beat_length = len(music_string)

    result = []
    for beat in range(notes["o"]):
        if beat_length == notes["o"] * 4:
            result.append(beat)
        beat_length -= 4

    for beat in range(notes["o"]):
        if beat_length == notes["o"] * 2:
            result.append(beat)
            beat_length -= 2

    for beat in range(notes["o"]):
        if beat_length == notes["|"]:
            result.append(beat)
            beat_length -= 1

    return result

# Test cases
test_parse_music = [
    "o o| .| o| .| .| .| .| o o",
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4],
    [("o", 4), ("o", 2), (".", 1)],
    [("o", 4), ("o", 2), ("o", 1), (".", 1)],
    [("o", 4), ("o", 2), "|", (".", 1)],
    [4, 2, 1, 2, 2, 1, 1, 1, 4, 4],
    [4, 2, 1, 2, 2, 1, 1, 1],
    [4, 2, 1, 2, 1, 2, 2, 1],
]

for music, expected, notes in test_parse_music:
    actual = parse_music(music)
    print(f"Music: {music}, Expected: {expected}, Notes: {notes}")
    print(f"Actual: {actual}")
    print(f"Distance: {[(actual[i] - expected[i]) for i in range(len(actual))]}")
```