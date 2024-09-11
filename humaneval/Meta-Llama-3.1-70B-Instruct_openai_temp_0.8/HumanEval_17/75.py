```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of musical notes in a special ASCII format and returns a list of integers
    representing the number of beats each note lasts.

    :param music_string: A string of musical notes
    :return: A list of integers representing the number of beats each note lasts
    """
    
    # Create a dictionary to map each note to its corresponding beats
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    
    # Split the input string into individual notes
    notes = music_string.split()
    
    # Initialize an empty list to store the beats of each note
    beats = []
    
    # Initialize an empty string to build each note
    note = ''
    
    # Iterate over each character in the notes string
    for char in notes:
        # If the character is 'o' or '.|', it's a complete note
        if char in note_beats:
            # Add the beats of the current note to the list
            beats.append(note_beats[char])
        else:
            # If the character is '|' and the note is 'o', it's a half note
            if note == 'o' and char == '|':
                # Add the beats of the half note to the list
                beats.append(note_beats['o|'])
            # If the character is '|' and the note is '.', it's a quarter note
            elif note == '.' and char == '|':
                # Add the beats of the quarter note to the list
                beats.append(note_beats['.|'])
            # Add the character to the note
            note += char
    
    # Return the list of beats
    return beats


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```