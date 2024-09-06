```python
import re

def parse_music(music_string: str) -> List[int]:
    # Regular expression to match a pattern of one of the four available notes.
    NOTE_PATTERN = re.compile(r'(?P<whole_note>o){1,2}'
                             r'(?P<half_note>o|)|'
                             r'(?P<quarter_note>.\.){1,2}')

    # Define dictionary to translate matches into integer note values.
    note_values = {'whole_note': 4, 'half_note': 2, 'quarter_note': 1}

    # Return list where each element is the length of a line from the input string.
    return [sum(note_values[match.group()] for match in NOTE_PATTERN.finditer(line))
            for line in music_string.split('\n')]
```

#### Explanation:
- A regular expression pattern is defined to match note patterns from the input string.
- It captures three possible patterns in the input:
    - `o` - whole note, lasts four beats. It can appear 1 or 2 times in a row.
    - `o|` - half note, lasts two beats. It can appear optionally, as `o` or `o|`.
    - `.` - quater note, lasts one beat. It can appear 1, 2, or 3 times in a row.
- A dictionary is defined to translate matched patterns into integer note values.
- The `parse_music` function splits the input string into lines using `split('\n')`, and for each line, it sums up 
    the note values, as computed by the list comprehension that iterates over each match group and looks up the 
    corresponding value in the note_values dictionary. 

This solution accepts any mix of quarter, half, and whole notes and any number of beats for each (as long as they 
satisfy the input constraints and are well-formed). 

It's important to note that this solution assumes the input constraints outlined in the problem statement, 
such as the number of beats per whole note (4), and doesn't account for other potential variations without 
further modifications.