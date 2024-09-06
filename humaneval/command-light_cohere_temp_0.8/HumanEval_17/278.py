```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    beats = [0] * 6  # Initialize beats for whole, half, quarter notes
    notes = ['o', 'o|', '|', 'o', 'o', '|', '.', 'o', 'o']  # List of musical notes

    for note in notes:
        found = music_string.find(note, 0)
        if found != -1:
            beats[found] += 1

    return beats

# Test the function
test_music = parse_music('o o| .| o| .| .| .| .| o o')
test_beats = parse_music('o o| o| .| o| .| .| .| o o')

# Print the results
print(test_music)
print(test_beats)
```
This code defines a function called **parse_music** that takes a music string as input and returns a list of beats corresponding to the notes in the music. The function uses a type hint for the music string to parse and return the beats.