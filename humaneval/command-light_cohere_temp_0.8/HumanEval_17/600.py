```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1}
    
    pattern = r'(\d+)\s+'
    matches = music_string.findall(pattern, music_string)

    return [int(match[0]) for match in matches]

# Test cases
test_data = [
    'o o| .| o| .| .| .| .| o o', [4, 2, 1, 2, 2, 1, 1, 1, 1, 4]
  ,  'o o| .| o| .| .| .| .| o o', [4, 2]
  ,  '.|' .|.' ,'.join, [1]
  ,  'o o o o o o| .| o o| .', [4, 4, 4]
  ,  'o o o o o o o o| .' .| .| o o', [4, 2, 4]
]

for data, expected in test_data:
    actual = parse_music(data)
    print(f'Expected: {expected}, Actual: {actual})
```