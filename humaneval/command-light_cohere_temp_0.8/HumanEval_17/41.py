Here is a self-contained Python function that solves the markdown code block problem:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    return [notes[ch] for ch in music_string.get()]
```

This function parses a string representing musical notes in a special ASCII format. It uses a legend where 'o' stands for whole notes, 'o|' stands for half notes, and '.'|' stands for quarter notes.