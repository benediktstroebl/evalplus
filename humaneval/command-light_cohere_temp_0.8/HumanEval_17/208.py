```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split(' '|')
    beat = 1
    notes = [int(note) for note in notes]

    def check_notes(notes: List[int]) -> bool:
        num_whole_notes = sum(1 for note in notes if note == 4)
        num_half_notes = sum(1 for note in notes if note == 2)
        num_quarter_notes = sum(1 for note in notes if note == 1)

        return num_whole_notes + num_half_notes == len(notes) and num_quarter_notes == 0

    return all(check_notes(notes)) for _ in range(3))

# Example usage
music_string = 'o o| |.| o| o' .| .| .| o o' o'
if parse_music(music_string) == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]:
    print("Function passed all tests")
```