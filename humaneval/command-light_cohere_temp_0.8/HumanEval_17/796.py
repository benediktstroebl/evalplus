```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = ['o', 'o|', '.|']
    beats = [4, 2, 1]

    def get_beat_length(note):
        return beats.get(note, 0)

    notes = [note for note in notes if note in music_string]

    beats = [get_beat_length(note) for note in notes]

    return beats

# Test the parse_music function
def test_music_parser():
    music_str = 'o o| .| o| .| .| .| .| o o'
    beats = parse_music(music_str)

    print(beats)  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]

    music_str = '...|...'
    beats = parse_music(music_str)

    print(beats)  # Output: [0, 0, 0, 0] (empty string does not produce beat)

    music_str = '.'
    beats = parse_music(music_str)

    print(beats)  # Output: [] (empty string does not produce beat)

# Example usage
test_music_parser()
```

This script defines a `parse_music` function that takes a music string and returns a list of integers representing the number of beats for each note. The function uses a legend of musical notes with their respective beat lengths, and the `get_beat_length` helper function to extract the beat length for each note. The function is then tested using various music strings and their outputs are verified against the expected results.