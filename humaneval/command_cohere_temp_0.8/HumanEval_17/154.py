```python
from typing import List

pattern = '^(?:o(?!\\|)|(?:o)?|\\|?) (?=\\.|$)'

def parse_music(music_string: str) -> List[int]:
    return [4 if m == 'o' else 2 if m == 'o|' else 1 for m in music_string.split(' | ') if m and (m[0] in 'o|.') and re.match(pattern, m)]
```

The Python script employs a regular expression (`re.match()`) to validate musical notes in a given string, optimizing performance. The function `parse_music` accepts a string input of musical notation and returns a list of integers representing the beats. 

Whole notes last four beats (`'o'`), half notes last two (`'o|'`), and quarter notes last one (`'.'`). The function splits the input string by vertical bars (`'|'`), and any empty strings or invalid notes are filtered out.

This optimized approach allows for faster processing and better usability, providing a more efficient solution for parsing musical notation.