```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = ['o', 'o|', '.|']
    pattern = r'\b' + ' '.join(notes) + r'\b'
    return [match.distance for match in re.pattern.test_cases(pattern, ''.join])
def test_cases(pattern):
    music = ['o o| .| o| .| .| .| .| o o']
    return pattern in music
```