```python
from typing import List

pattern = '^ {0,2}(?:o|O|[.||]) ({1,3})?$'

def parse_music(music_string: str) -> List[int]:
    """ Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return list of integers corresponding to how many beats does each
    not last.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    >>> parse_music('o o| .| o| o| .| .| .| .| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    def note_duration(char: str) -> int:
        if char == 'o' or char == 'O':
            return 4
        if char == '|' or char == ' ':
            return 2
        return 1
    
    # regex pattern to check if string is a valid music string
    if not re.match(pattern, music_string):
        raise ValueError("Invalid music string")
    
    return [note_duration(char) for char in music_string]
```

This code defines a function `parse_music` that takes a string input and returns a list of integers representing the beats of each note. The function first uses a regular expression pattern to match the input string and make sure it is a valid music string. Then, it iterates over each character in the string, and uses a dictionary lookup to determine the duration of each note, based on its character. Finally, the function returns a list of integers, where each integer corresponds to the number of beats for the note with that character. 

To make sure the solution is correct, it is recommended to add unit tests that cover different cases, like empty strings, only whole notes, or a mix of all possible notes.  Here is an example of a unit test:
```python
def test_parse_music():
    # Arrange
    music = "o o| .| o| o| .| .| .| .| o o"

    # Act
    beats = parse_music(music)

    # Assert
    assert beats == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4], "Failed to parse music string correctly"
``` 
This test case verifies that the `parse_music` function correctly converts the given music string into a list of beat durations.