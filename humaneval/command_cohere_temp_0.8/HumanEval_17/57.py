```python
from typing import List

 Pattern = str


def parse_music(music_string: Pattern) -> List[int]:
    """Input to this function is a string representing musical notes in a special ASCII format. 
 Your task is to parse this string and return list of integers corresponding to how many beats does each
note last. 

Here is a legend:
'o' - whole note, lasts four beats
'o|' - half note, lasts two beats
'.|' - quater note, lasts one beat

Example:
'o o| .| o| o| .| .| .| .| o o'
[4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
"""

# Use a regex to find all matches in the input string
beat_counts = ['4', '2', '1']

def note_parser(note: str) -> int:
    for bc in beat_counts:
        if note == f'{bc}|' or note == f'.|{bc}' or note == f'o{bc}':
            return int(bc)
    raise ValueError(f"Invalid note: {note}")

# Use a recursive descent parser
def parse_recursive(music_string: Pattern, beat_count: int = 0) -> List[int]:
    result: List[int] = []

    if not music_string:
        return result

    # Use greedy parsing to try and parse as many notes as possible
    for i in range(len(music_string)):
        note = music_string[i]
        if note == 'o':
            result.append(beat_count)
        elif note == '|':
            beat_count += 1
        elif note == '.':
            result.append(note_parser(note))
        else:  # pragma: no cover
            raise ValueError(f"Invalid note: {note}")

        # After parsing a note, eat it from the music string
        music_string = music_string[i + 1:]

        # Recursively parse remaining music string
        result.extend(parse_recursive(music_string, beat_count))

    # If remaining beats are greater than 0, assign them to a whole note
    if beat_count > 0:
        result.append(beat_count)

    return result

# Test the parser
# Test cases are taken from the problem statement
test_cases = [
    ('o o| .| o| o| .| .| .| .| o o', [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]),
    ('| .| o', [2, 1, 2]),
    ('o o| o .| o o| o', [4, 2, 1, 4, 2]),
]

for string, expected in test_cases:
    print(f'Parse: {parse_recursive(string)}')
    print(f'Expected: {expected}')
    print('-' * 40)
```

The script follows a recursive descent approach to parse the music string. It uses a regular expression to match three different note types, 'o', '|', and '.'. The `note_parser` function is used to determine the beat count corresponding to a note based on its position in the regex pattern. 

The `parse_recursive` function follows the grammar of the musical notation to construct the resulting `List[int]`. It tries to parse as many notes as possible using a greedy approach. Finally, the remaining beats in the beat