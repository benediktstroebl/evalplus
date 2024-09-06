```python
import re

def parse_music(music_string: str) -> List[int]:
    # Regular expression to match a pattern of one of the four available notes.
    NOTE_PATTERN = re.compile(r'(?P<whole_note>o)|(?P<half_note>o\|)|(?P<quarter_note>.\|)'
                             r'(?P<dot_rest>\.|(?=\)))')

    # Example string with all the notes and a rest.
    example_string = 'o o| .| o| o| .| .| .| .| o o'

    # Calculate the length of the whole note by multiplying the number of beats with the note length.
    whole_note_length = 4

    # List to store the number of beats for each note.
    note_beats = []

    for match in NOTE_PATTERN.finditer(music_string):
        note_length = None
        note_value = None

        # Get the length of the note depending on the match.
        if match.group('whole_note'):
            note_length = whole_note_length
        elif match.group('half_note'):
            note_length = 2
        elif match.group('quarter_note'):
            note_length = 1

        if match.group('dot_rest') is None:
            # Multiply the length of the note by the number of occurrences of this note.
            note_value = note_length * len(match.group())
        note_beats.extend([note_value] * len(match.group()))

    return note_beats
```

#### How it works:
1. The regular expression `NOTE_PATTERN` matches three patterns:
    - Whole note `o`
    - Half note `o|`
    - Quarter note `.|`
2. The code calculates the length of a whole note by multiplying the `beat` coefficient with the `note_length`,
   defining it as `whole_note_length`.
3. The `NOTE_PATTERN` is applied to the `music_string` using the `finditer` method, iterating through every match of the
   pattern.
4. For each match, the code checks the value of the captured group to determine the length of the note, then
   multiplies it by the number of occurrences of the note.
5. The resulting values are added to a list and returned.

The given example is used to showcase the function and demonstrates how the beats are calculated for each note.

**NOTE**: The code assumes that each note/rest is separated by a single space. It may not work as expected for strings
containing multiple spaces between notes/rests. Additional preprocessing could be required in such cases.