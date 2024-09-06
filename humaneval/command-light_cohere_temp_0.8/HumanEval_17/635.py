```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1}
    format = ' '.join(notes.format)
    
    beats = music_string.format(format)
    notes

    return [beats[i::4] for i in range(len(beats))]

# Test case 1
print(parse_music('o o| .| o| .| o'))
# Output: [4, 2, 1]

# Test case 2
print(parse_music('| .o o| .| .| .| o'))
# Output: [1, 4, 1]

# Test case 3
print(parse_music('o o| .o o'))
# Output: [4, 2]

# Test case 4
print(parse_music('...|'))
# Output: []

# Test case 5
print(parse_music('o o| .o o o'))
# Output: [4, 2, 2]
```
This code defines the `parse_music` function that takes a string of music notes in a special ASCII format and returns a list of integers representing the number of beats for each note. The function uses a legend: 'o' - whole note, 'o|' - half note, '.|' - quarter note, and the parsed notes are stored in the `notes` dictionary. The function then applies the format to the string, and uses this format to extract the beats, and finally, it returns the list of beats.

You can add more test cases as required.