```python
from typing import List

pattern = 'o|_|.'
beats = {
    'o': 4,
    '|': 2,
    '._': 1,
}

def parse_music(music_string: str) -> List[int]:
    music_list = [beats[char] for char in music_string if char in pattern]
    return music_list
```

The problem is solved using a dictionary called `beats` which maps each character in the string to the number of beats it represents. The `parse_music` function uses a list comprehension to traverse each character in the string, checking if each character is in the `pattern` and then mapping it to its corresponding number of beats in the `beats` dictionary. 

This solution is efficient and can parse strings of varying lengths of musical strings. It achieves this without any unnecessary complexity or constraints on the input. 

Such solutions demonstrate the utility of the `typing` module, and provide an elegant solution to parsing problems.