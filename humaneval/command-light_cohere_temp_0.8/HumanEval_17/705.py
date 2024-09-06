```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = ['o', 'o|', '.|']
    duration = [1, 2, 4]
    pattern = ''.join|'.join
    result = []
    for beat in range(1, 6):
        for note in notes:
            count = pattern.find(music_string, note)
            if count is not None:
                result.append(duration[beat] * count)
    return result
def test_music():
    music_str = 'o o| .| o| .| .| .| .| o o'
    result = parse_music(music_str)
    assert len(result) == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```