```python
import re

def parse_music(music_string: str) -> List[int]:
    # Regular expression to match a pattern of one of the four notes
    note_pattern = r'(?P<whole_note>o)|(?P<half_note>o\|)|(?P<quarter_note>.\|)'

    # Using recursive regex to extract all notes from the string
    beats = []
    for match in re.finditer(note_pattern, music_string):
        note = match.group()
        if note == 'o':
            beats.append(4)
        elif note == 'o|':
            beats.append(2)
        elif note == '.|':
            beats.append(1)
        else:
            beats.append(0) # Unknown note, default to 0 beats
    return beats
```

To understand the logic of the code above, pay attention to these points:
1. We define a regular expression note_pattern that matches one of the three note types. 
 2. Then, the re.finditer function finds all occurrences of note_pattern in the input music_string. 
 3. For each match, we extract the specific note using match.group(), and we assign the corresponding number of beats. 
4. If the note type is unknown, we default to 0 beats in the resulting list. 

The provided example and tests demonstrate how the function works with different inputs. Feel free to customize the function further based on your requirements. Let me know if you have any other questions!