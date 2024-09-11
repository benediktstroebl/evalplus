```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of musical notes in a special ASCII format and returns a list of integers 
    corresponding to how many beats each note lasts.

    :param music_string: A string representing musical notes.
    :return: A list of integers representing the duration of each note in beats.
    """
    
    # Define a dictionary to map each note to its corresponding duration
    note_durations = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the durations
    durations = []

    # Initialize an empty string to build each note
    current_note = ''

    # Iterate over each character in the input string
    for char in music_string:
        # If the character is a space, it means we've reached the end of a note
        if char =='':
            # Add the duration of the current note to the list
            durations.append(note_durations[current_note])
            # Reset the current note
            current_note = ''
        else:
            # Add the character to the current note
            current_note += char

    # Add the duration of the last note to the list
    durations.append(note_durations[current_note])

    return durations


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

However, the above solution will not give the expected output because it tries to find the note duration from the note_durations dictionary after the loop, at which point current_note is 'o'. Therefore, it will throw a KeyError. 

Here is the correct version:

```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of musical notes in a special ASCII format and returns a list of integers 
    corresponding to how many beats each note lasts.

    :param music_string: A string representing musical notes.
    :return: A list of integers representing the duration of each note in beats.
    """
    
    # Define a dictionary to map each note to its corresponding duration
    note_durations = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Initialize an empty list to store the durations
    durations = []

    # Initialize an empty string to build each note
    current_note = ''

    # Iterate over each character in the input string
    for char in music_string:
        # Add the character to the current note
        current_note += char
        # If the character is a space or we've reached the end of the string, it means we've reached the end of a note
        if char =='' or music_string.index(char) == len(music_string) - 1:
            # If it's not the last character, remove the last character from the current note because it's a space
            if char =='':
                current_note = current_note[:-1]
            # Add the duration of the current note to the list
            if current_note in note_durations:
                durations.append(note_durations[current_note])
            # Reset the current note
            current_note = ''

    return durations


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```