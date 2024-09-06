```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = ['o', 'o','.', '|','.']
    durations = [1, 2, 4, 4]  # whole, half, quarter, rest

    pattern = r'(\+? +| \1| \4| \4|) (.+\s+)'
    matches = re.sub(pattern, music_string, lambda match: [int(match.group(1)), durations]

    return [note[0] * beats for note, beats in note] for note in notes]

# Test cases
test_cases = [
    "o o| .| o| .| .| .| o o",
    "o o| .| .| o| o",
    ".",
    "o o| ",
    " ",
    "| ".o",
    ". o| o",
]

for case in test_cases:
    actual = parse_music(case)
    assert actual == [4, 2, 1, 2, 1, 1, 1, 1, 4, 4], case  # Check the correct beat count for each note

This script defines a function `parse_music` that parses a music string and returns a list of beat counts. The function uses regular expressions to identify the different note types and their durations, and then multiplies the durations by the corresponding note to get the total number of beats for that note. 

Test cases are provided to check the correctness of the `parse_music` function.