Here's a self-contained Python script that includes the `parse_music` function along with its tests:

```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format.
    Format: 
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat
    ' ' - note (any other character)
    [beat]
    >>> parse_music('o o| .| o| .| .| .| .| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4]
    """
    # Split the string by whitespace and notes
    music_notes = music_string.split(' '|')

    # Initialize an empty list
    note_beat = []

    # Loop through each note
    for note in music_notes:
        if note.isalpha():  # Convert the example, we want whole notes. Half notes have 1 and notation, the bar symbol is escaped ('|').
        # If the current note is not a whole note, append it to the list
        note_beat.append(1)

    # Return the list of beats
    return note_beat

# Test cases
def test_music():
    music_str = 'o o| .| o| .| .| .| .| o o'
    result = parse_music(music_str)
    assert len(result) == len(music_str.split(' '|'))
    assert result == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4]

if __name__ == "__main__":
    test_music()
```

This code contains a function `parse_music` that parses a string of musical notes and returns a list of integers representing the number of beats in each note. The function is then split the input string into individual notes and then loops through each note, appending the appropriate number of beats to a list.

The code also includes test cases to verify the correctness of the `parse_music` function.