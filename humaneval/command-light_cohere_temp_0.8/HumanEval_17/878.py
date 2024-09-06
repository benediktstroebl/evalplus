```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1, 'o' : 4}
    return [notes[ch] for ch in music_string.print(notes)
```

The code defines a function named `parse_music` that takes a string music_string as input and returns a list of integers. The function uses a dictionary `notes` to map musical notes to the number of beats each note lasts, and uses the `print` function to iterate through each character in the music_string and assigns the character to the number of beats it lasts. 
Finally, the function returns the resulting list of integers.