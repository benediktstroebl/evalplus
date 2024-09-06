```python
from typing import List

PATTERN = "/(?P<whole>o)(?P<half>o|)|(?P<quarter>.)/"

def parse_music(music_string: str) -> List[int]:
    return [len(re.findall(PATTERN, e)) for e in music_string.split(' ')]
```

The provided Python script solves the problem by using regular expressions. 

Here is an explanation of each part of the code:
- The `from typing import List` import is used to ensure the function returns a list of integers. 
- The `PATTERN` variable is a regular expression pattern used to match the different types of notes. `o` matches a whole note, `o|` matches a half note, and `.|` matches a quarter note. The slashes `/` denote the beginning and end of the pattern.
- The `re.findall()` function finds all occurrences of the pattern in the input string and returns them as a list. The `len()` function is then used to count the number of beats.

The script then returns the list of integers corresponding to the number of beats for each note.