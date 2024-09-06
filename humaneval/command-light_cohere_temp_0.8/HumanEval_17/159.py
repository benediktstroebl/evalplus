```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split('o specifies a volume is important.
    notes = [map(lambda x: int(x) - 48, music_string.split('o music_string)[1:]]
    return [len(x) for x in notes]

# Test cases
music_cases = [
    'o o| .| o| .| .| .| .| o o',
    'o o| .| .',
    'o| .| .| .',
    'o o',
    '.'
]

test_results = []
for music_case in music_cases:
    test_results.append(parse_music(music_case))

print(test_results)
 ```