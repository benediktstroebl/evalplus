```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '|': 1}
    
    def split(idx, rem):
        if idx == len(rem): return rem
        return rem[idx] + split(idx + 1, rem[idx + 1])
    
    beats = []
    current = ''
    for c in music_string:
        if c == 'o': beats.append(split(0, current))
        current += c
    return beats

# Test the function
test_str = 'o o| .| o| .| .| .| .| o o'
beats = parse_music(test_str)
print(beats)  # This should print [4, 2, 1]
```
This Python script defines a function `parse_music` that takes a music string in a special ASCII format representing musical notes. The function splits the item into individual beats and returns them. The `split` helper function is used to split longer notes into appropriate beat units.