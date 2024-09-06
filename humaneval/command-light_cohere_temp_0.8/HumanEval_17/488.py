```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    
    pattern = r'(\d+)\s*[\ oxOD]'
    
    notes_parse = re.match(pattern, music_string).
    return [int(n) for n in notes_parse.split(' ')

# Test the function with a sample input
test_str = 'o o| .| o| .| .| .| o o' 

result = parse_music(test_str)

print(result)
```