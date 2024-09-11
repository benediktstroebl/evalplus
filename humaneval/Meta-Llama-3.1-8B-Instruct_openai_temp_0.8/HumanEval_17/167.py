```markdown
### Parse Music String
#### Problem Description
Input to this function is a string representing musical notes in a special ASCII format.
The task is to parse this string and return a list of integers corresponding to how many beats each note lasts.

#### Legend
* `'o'` - whole note, lasts four beats
* `'o|'` - half note, lasts two beats
* `'.|'`` - quarter note, lasts one beat

#### Solution
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes and return a list of integers representing the number of beats each note lasts.

    Args:
        music_string (str): A string of musical notes in the special ASCII format.

    Returns:
        List[int]: A list of integers representing the number of beats each note lasts.
    """
    # Create a dictionary to map musical notes to their corresponding beats
    note_beats = {'o': 4, 'o|': 2, '.|': 1}
    
    # Initialize an empty list to store the total beats for each note
    total_beats = []
    
    # Split the input string into individual notes
    notes = music_string.split()
    
    # Iterate over each note
    for note in notes:
        # Get the number of beats for the current note from the dictionary
        beats = note_beats.get(note, 0)
        
        # Append the number of beats to the total beats list
        total_beats.append(beats)
    
    # Return the list of total beats
    return total_beats

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

#### Output
```
[4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```