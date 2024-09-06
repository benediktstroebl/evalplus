```python
import re

def parse_music(music_string: str) -> List[int]:
    beat_pattern = re.compile(r'o+(?=\||.*)|o|.|o+')
    return [len(x.group()) for x in beat_pattern.finditer(music_string)]
```

This approach utilizes Python's regular expression and its re module. Regular expression, or regex, is a sequence of characters that forms a search pattern. They can be used to check if a string contains the specified search pattern.

The beat_pattern regex search string contains three different patterns that represent the three different musical notes:
1. `o+(?=\||.*)` - This pattern matches a string of 'o' characters that are followed by a vertical bar '|' or a dot '.' 
2. This is achieved due to the syntax `(?=\||.*)` which translates to "lookahead", it checks if the next character(s) after o+ is a vertical bar '|' or a dot '.' 
2. `o|.|o+` - This pattern simply matches a single character:
   - 'o' - Whole note occupies four beats.
   - '|' - Half note occupies two beats.
   - '.' - Quarter note occupies one beat. 

The function iterates over the match objects created by finding all instances of the pattern in the input string using `re.finditer()`. The match object contains useful methods to retrieve the captured groups or other attributes of the matched strings. In this case, the length of the first captured group (the beats) is returned for each match.