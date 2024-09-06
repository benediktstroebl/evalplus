```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    beats = [int(x) for x in music_string.split('oora ')
    whole_notes = music_string.split('o+o whole_notes
quarter_notes = music_string.split('.' music_string.split('o opened')
quarter_notes
half_notes = music_string.split('/2')
notes = quarter_notes + whole_notes

return [len(quarter_notes) * 4, * len(quarter_notes) + len(whole_notes), * len(quarter_notes), * len(half_notes)]

# Test cases go here too!
# Example:
music_string = 'o o| .| o| .| .| .| .| .| o o'
result = parse_music(music_string)
print(result)
```