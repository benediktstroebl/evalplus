```python
from typing import List

Pattern = str
Notes = List[int]


def parse_music(music_string: Pattern) -> Notes:
    beat = 4
    notes = []
    parts = music_string.split('|')
    for n in parts:
        if 'o' == n:
            notes.append(beat)
        elif '.' != n:
            notes.append(int(n[1]) * beat)
        beat //= 2
    return notes
```

The beat variable is initialized to 4 and serves as a beat count for a whole note 'o'. Each note is either a whole note or halves, quarters, etc. This is based on the position of the digit, where the beat is divided by 2, or on the digit value, which directly reduces the beat count.

The code structure is very simple, and easy to understand. It can be improved with error handling to ensure the input format, but this solution is already quite complete.

This script adheres to the type hints in the problem statement, using `List` and `str` from the typing module, and defines new type hints for the function parameters and return value. This is not only for better readability but also for strict enforcements in some development environments, like MyPy. 

The function `parse_music` takes a string input and returns a list of integers (the number of beats per note). Test cases are not included, but this code can be tested with the provided test cases in the problem statement.