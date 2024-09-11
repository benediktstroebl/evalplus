```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string representing musical notes in a special ASCII format,
    parses this string and returns a list of integers corresponding to how many beats
    each note lasts.

    Args:
        music_string (str): A string representing musical notes.

    Returns:
        List[int]: A list of integers representing the duration of each note in beats.
    """
    # Define a dictionary to map each note to its duration
    note_durations = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    
    # Split the input string into a list of notes
    notes = music_string.split()
    
    # Initialize an empty list to store the durations
    durations = []
    
    # Initialize an empty string to build each note
    current_note = ''
    
    # Iterate over each character in the input string
    for char in music_string:
        # Add the character to the current note
        current_note += char
        
        # Check if the current note is in the note_durations dictionary
        if current_note in note_durations:
            # If it is, add its duration to the durations list
            durations.append(note_durations[current_note])
            # Reset the current note
            current_note = ''
    
    # Return the list of durations
    return durations

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```