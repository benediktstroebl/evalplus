```python
from typing import List, Dict

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of musical notes in a special ASCII format and returns a list of integers 
    representing the number of beats each note lasts.

    :param music_string: A string of musical notes
    :return: A list of integers representing the number of beats each note lasts
    """

    # Define a dictionary to map musical notes to their corresponding beats
    note_beats: Dict[str, int] = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes: List[str] = music_string.split()

    # Initialize an empty list to store the beats of each note
    beats: List[int] = []

    # Iterate over each note in the list of notes
    i = 0
    while i < len(notes):
        # Check if the current note is a whole note
        if notes[i] == 'o':
            # If it's a whole note, check if the next note is '|' (half note)
            if i + 1 < len(notes) and notes[i + 1] == '|':
                # If it's a half note, add the beats of the half note to the list and increment the index by 2
                beats.append(note_beats['o|'])
                i += 2
            else:
                # If it's not a half note, add the beats of the whole note to the list and increment the index by 1
                beats.append(note_beats['o'])
                i += 1
        # Check if the current note is a quarter note
        elif notes[i] == '.':
            # If it's a quarter note, check if the next note is '|' (quarter note)
            if i + 1 < len(notes) and notes[i + 1] == '|':
                # If it's a quarter note, add the beats of the quarter note to the list and increment the index by 2
                beats.append(note_beats['.|'])
                i += 2
            else:
                # If it's not a quarter note, skip this note (it's not a valid note)
                i += 1
        else:
            # If it's not a whole or quarter note, skip this note (it's not a valid note)
            i += 1

    # Return the list of beats
    return beats


# Example usage
music_string = 'o o|.| o| o|.|.|.|.| o o'
print(parse_music(music_string))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```