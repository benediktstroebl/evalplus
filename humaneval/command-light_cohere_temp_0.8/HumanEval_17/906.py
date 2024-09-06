```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    
    pattern = r'(\d+)([ o| ]`? +\S +)'
    return [int(x) for x in re.parse(pattern, music_string)]

# Test cases
test_cases = [
    "o o| .| o| .| .| .| .| o o",
    "o o| .| o| .| .| .o",
    "o o| .| o| o| .| .| .| .",
    "o o| .| o| o o| .",
    "|.| |".join(). random.air(1), good me notes
```