```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1}
    beats = [notes[c] for c in music_string.split('.') if c in music_string and c in notes]
    return beats

def test_parse_music() -> None:
    assert parse_music('o o| .| o| .| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    assert parse_music('x') is []
    assert parse_music('.a') == []
    bandit = parse_music('o o| .| o| .| .| .| .| o o')
    print(bandit)
    assert len(bandit) == 4 and all(beat == 4 for beat in bandit)
    assert len(bandit) == 2 and all(beat == 2 for beat in bandit)
    assert len(bandit) == 1 and all(beat == 1 for beat in bandit)
    assert len(bandit) == 4
    assert all(beat == 4 for beat in bandit)

if __name__ == "__main__":
    test_parse_music()
```
The provided Python script defines a function `parse_music` that takes a music string in a specific format and returns a list of integers representing the number of beats corresponding to each note. The function then uses a predefined dictionary `notes` to map the musical notes to the corresponding beat values. The test_parse_music function contains a series of assertions that verify the correctness of the `parse_music` function.