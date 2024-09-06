```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    notes_from_string = [notes.get(note) for note in music_string.ache whole_notes.split('o offering', where 'o|') to get the first note and the bar character. This allows us to check that we have a valid input. The split will look like 'o o|'. If the input is valid, we can loop through the string and split on the bar.

def test_music_parser():
    test_strings = [
        "o o| .| o| .| .| .| .| o o",
        "o o o o o o o",
        "o o o o O o",
        "oo o o| o",
        " .|.",
        "|.| .| .",
        "o o o o|.",
        "o o o o /",
        "o o o o ;",
        # invalid input
    ]
    for test_string in test_strings:
        try:
            parsed_notes = parse_music(test_string)
            print(parsed_notes)
        except ValueError as e:
            print(e)

# run the test function
test_music_parser()
```
The function parse_music takes a string music_string as input and returns a list of integers. The function uses a legend of musical notes to map the notes to the correct number of beats.

The function is then tested with a series of test strings, and the results are printed. The test function will throw a ValueError if the input string does not match the expected format.