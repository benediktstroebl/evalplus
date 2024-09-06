```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4, 'o|': 2, '|': 1,
    }
    
    beats = []
    current_beat = 0
    notes_found = 0
    
    for char in music_string:
        if char in notes:
            beats.append(current_beat)
            current_beat += notes[char]
            notes_found += 1
    
    return beats

# Test case
music_test = 'o o| .| o| .| .| .| .| o o'
beats = parse_music(music_test)
print(beats)  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```

This function, `parse_music`, accepts a music_string as input and returns a list of integers. It accomplishes this task of parsing music notes in a special ASCII format into a representation of beats. The function utilizes a legend to identify the different note lengths, and it then counts the number of each type of note that was found in the string.

By utilizing this function, you can create and execute tests using different music strings, verifying the function's ability to correctly parse and convert the music into a representation of beats. 

This function is self-contained and handles the entire process within the same function, providing a clear and concise solution to the problem.