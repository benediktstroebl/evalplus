```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = music_string.split(' ') '
    whole notes only contain 'o' and can be as long as desired. we'll create a count how many whole notes, splitting them by 'o' or '|' to account for half notes. Here's test the example, we'll use a music string with different note lengths: 
    'o o| .| o| .| .| .| .| .| o o'
    Each whole note and half note will be added to the notes list, with their corresponding count.

In this function, we're using Python's string.split method to split the music_string by ' ', assuming that the space is used to separate the music.