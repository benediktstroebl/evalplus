```python
import re

def parse_music(music_string: str) -> List[int]:
    # Regular expression to match a pattern in the music string
    pattern = re.compile(r'o|' +
                          r'(.)|' +
                          r'o\|' +
                          r'(.)|' +
                          r'.|' +
                          r'o|.' +
                          r'{2,}',
                        flags=re.I)

    # Creating a list to store beats
    beats = []

    # For each match of the regular expression...
    for match in pattern.finditer(music_string):
        # ...checking the length of the previous match to determine the beats
        if match.group(1) == 'o':
            beats.append(4)
        elif match.group(1) == match.group(3):
            beats.append(1)
        else:
            beats.append(2)

    return beats
```

The provided Python script defines a function called `parse_music` that takes a string input parameter called `music_string`. This string represents musical notes in a special ASCII format. The function's purpose is to parse this string and return a list of integers representing the number of beats each note lasts.

To achieve this, the function utilizes a regular expression pattern formulated with the `re.compile` function. The pattern identifies the different note types within the music string: 'o' for whole notes, '|' for half notes, '.' for quarter notes, 'o|' for half-dotted quarter notes, and '.|' for eighth notes.

The function iterates through each match of this regular expression, determining the length of the previous match to assign the appropriate number of beats to the current note. Specifically, whole notes are assigned 4 beats, half notes 2 beats, and quarter notes 1 beat. Any other combination of note lengths is treated as a half note.

The resulting list of beats is stored in the `beats` list, which is returned by the function.