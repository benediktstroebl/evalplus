### Music Note Parser
#### Parse Music Notes from ASCII String
```python
from typing import List


def parse_music(music_string: str) -> List[int]:
    """
    Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return list of integers corresponding to how many beats does each
    note last.

    Legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat

    :param music_string: A string representing musical notes in ASCII format
    :return: A list of integers corresponding to the beats each note lasts
    """
    # Define a dictionary to map notes to their corresponding beats
    note_beats = {'o': 4, 'o|': 2, '.|': 1}
    
    # Initialize an empty list to store the beats
    beats = []
    
    # Split the input string into individual notes
    notes = music_string.split()
    
    # Iterate over each note
    for note in notes:
        # Append the beats for the current note to the list
        beats.append(note_beats[note])
    
    # Return the list of beats
    return beats


# Example usage
music_string = 'o o|.| o| o|.|.|.|.| o o'
print(parse_music(music_string))
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```
This script defines a function `parse_music` that takes a string of musical notes as input, parses the string, and returns a list of integers representing the beats each note lasts. The function uses a dictionary to map notes to their corresponding beats, splits the input string into individual notes, and appends the beats for each note to a list. The script also includes an example usage of the function.