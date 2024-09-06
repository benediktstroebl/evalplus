```python
from typing import List

 Pattern = str


def parse_music(music_string: Pattern) -> List[int]:
    BEAT = {'o': 4, 'o|': 2, '.|': 1}
    return [BEAT[note] for note in music_string]
```

The following tests will check if the script correctly answers the problem:
```python
def test_parse_music():
    assert parse_music('o o| .| o| o| .| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    assert parse_music('o o') == [4, 4]
    assert parse_music('o| o| .|') == [2, 4, 1]
    assert parse_music('o| .| .| o') == [4, 1, 1, 2]
    assert parse_music('...| o.|..') == [1, 2, 1, 1, 1]
```

The `BEAT` dictionary can be used to lookup the number of beats corresponding to a particular note. The function iterates over each note in the `music_string` and extracts the corresponding number of beats using the `BEAT` dictionary. The returned list corresponds to the beats per note in the provided ASCII music string.

You can verify these test cases by adding an import statement at the top of the code snippet:
```python
import unittest
import parse_music  # Assuming you save the code in a file called parse_music.py

class TestParseMusic(unittest.TestCase):
    def test_parse_music(self):
        # Add test cases here, and they will run automatically
        test_parse_music.test_parse_music()
```