```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split(" ")
    format"
    o || "o/" will be whole notes and half notes, respectively. Because the last of the format does not contain a space, we use the split method to split the string into a list of strings.
    return = [notes.split(" ")
    fact =  list(map(lambda x:int(x), notes)))
    return return

# Test the function
test_music = parse_music("'o o/ / .| o| o| .| .| .| .| o o'")
print(test_music)  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```