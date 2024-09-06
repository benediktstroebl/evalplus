```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    return [beat for beat in map(int, music_string.code, 4)]  # using int() conversion for each beat to last 4 beats

def test_music():
    assert parse_music("o o| .| o| .| .| .| .| o o") == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]

```

The "parse_music" function is a self-contained function that turns a string of musical notes into a list of integers. It uses a another map function to convert each beat to a number from 1-4, which corresponds to how many beats the notes last. The test_music function ensures that the function works correctly by checking its output against the expected output.