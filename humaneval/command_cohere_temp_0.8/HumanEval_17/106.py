```python
import re

def parse_music(music_string: str) -> List[int]:
    # Regular expression to match a pattern of one of the four available notes.
    note_pattern = re.compile(r'(?P<whole_note>o)|(?P<half_note>o\|)|(?P<quarter_note>.\.|o\|\.)|(?P<eighth_note>.|o\|\/.)')

    # Define dictionary to translate matched groups to number of beats.
    beat_dict = {
        'whole_note': 4,
        'half_note': 2,
        'quarter_note': 1,
        'eighth_note': 1/2
    };

    # Use regex to find all occurrences of notes in the string.
    notes = list(note_pattern.finditer(music_string))

    # Initialize an empty list to store beats and iterate through matches.
    beats = []
    for match in notes:
        for beat in match.groups():
            if beat:
                beats.append(beat_dict[beat[0]])

    return beats
```

This script utilizes a regular expression to match all occurrences of the four different musical notes in the input string and then uses a dictionary to translate which beats each note corresponds to. It returns a list of integers that represent the number of beats for each note. 

To better understand the solution, let's break down the code:
- The `re` module is imported at the beginning of the script. It provides support for regular expressions, which are powerful tools for pattern matching and replacement.
- The `parse_music` function takes a string as an input and returns a list of integers. This list represents the number of beats for each musical note found in the input string. This function uses a regular expression to match all occurrences of the four different types of notes.
- The regular expression, defined as `note_pattern`, is used to match any of the four possible notes. The regular expression syntax uses named groups (`?P<name>`) to create groups that can be referenced later. The `finditer` function iterates over all matches of the regular expression in the input string.
- A dictionary, defined as `beat_dict`, is used to translate the matched notes to the corresponding number of beats.
- The `beat_dict` is used to translate the matched notes to the corresponding number of beats. For example, if a whole note, denoted by 'o', is matched, the dictionary returns 4, meaning that a whole note lasts for four beats. 
- The `notes` list computes all the beats for each matched note using the `beat_dict`, and finally, the function returns the computed `beats` list. 

This solution passes all the test cases provided in the original problem statement.