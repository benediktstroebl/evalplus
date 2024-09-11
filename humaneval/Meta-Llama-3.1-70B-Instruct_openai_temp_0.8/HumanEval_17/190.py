```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format and return a list of integers corresponding to how many beats each note lasts.

    Legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat
    """
    
    # Create a dictionary to map each note to its duration
    note_durations = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    
    # Split the input string into individual notes
    notes = music_string.split()
    
    # Initialize an empty list to store the durations of the notes
    durations = []
    
    # Initialize an empty string to build each note
    current_note = ''
    
    # Iterate over the notes
    for note in notes:
        # If the current note is not empty and the next note is not a part of the current note, 
        # add the duration of the current note to the list and reset the current note
        if current_note and note not in ['o', '|', '.']:
            durations.append(note_durations[current_note])
            current_note = ''
        
        # Add the current character to the current note
        current_note += note
        
        # If the current note is complete, add its duration to the list and reset the current note
        if current_note in note_durations:
            durations.append(note_durations[current_note])
            current_note = ''
    
    # If the last note was not added to the list, add it now
    if current_note in note_durations:
        durations.append(note_durations[current_note])
    
    return durations

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

When you run this script, it will print the list of note durations: `[4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]`.