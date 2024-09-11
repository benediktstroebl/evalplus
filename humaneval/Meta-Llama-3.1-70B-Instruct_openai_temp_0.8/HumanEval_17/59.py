```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string representing musical notes in a special ASCII format,
    parses this string and returns a list of integers corresponding to how many beats each note lasts.

    :param music_string: A string representing musical notes
    :return: A list of integers corresponding to how many beats each note lasts
    """
    
    # Create a dictionary to map notes to their corresponding beats
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    
    # Split the input string into a list of notes
    notes = music_string.split()
    
    # Initialize an empty list to store the beats of each note
    beats = []
    
    # Iterate over each note in the list of notes
    i = 0
    while i < len(notes):
        # Check if the current note and the next one form a note with a line
        if i + 1 < len(notes) and notes[i+1] == '|':
            # If so, append the beats of this note to the list and skip the next note
            beats.append(note_beats[notes[i] + notes[i+1]])
            i += 2
        else:
            # If not, append the beats of this note to the list
            beats.append(note_beats[notes[i]])
            i += 1
    
    # Return the list of beats
    return beats


# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```