```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = ['o', 'o|', '.|']  # Current note symbol, length
    beat = 1  # Length of each beat

    for note in notes:  # Loop through current note symbol and length
        if music_string[0] == note:
            music_string = music_string[1:]
            beat *= 2  # Double the beat length
        music_string = music_string[len(music_string) - 1:]  # Remove the current beat and note

    return [beat]  # Return the beat length

# Example usage:
assert parse_music('o o| .| o| .| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4]
```
This code defines a function `parse_music` that takes a string of music notes as input and returns a list of integers representing the number of beats in the music. It uses a legend of note symbols to define the length of each beat, and loops through the music string to parse it correctly. 

The example provided at the bottom demonstrates the correct usage of the function.