```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        "o": 4,
        "o|": 2,
        ".":": 1,
        ".":": 4,
        ".":|": 4,
        ".;": 1,
    }
    beats = music_string.split(" ")
    so far(beats)
    notes_indices = [notes.index(beat) for beat in beats]
    return [notes_indices[i] for i in range(len(beats))]

# Test the function
test_music = "o o| .| o| .| .| .| o o"
test_result = parse_music(test_music)
print(test_result)
``` 
This script defines a function parse_music that takes a music string in the format of the test case. It uses a notes dictionary that maps musical notes to the number of beats each one lasts. The function splits the music into a list of beats and then uses this information to create a list of the indices of the notes in each beat. 

The test_music variable is set to a sample music string, and the test_result variable is assigned the result of calling the parse_music function with the test_music string. Finally, the test_result is printed, which should contain the expected output, which is a list of indices corresponding to each beat.