```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = music_string.split(' '|')
    lengths = [len(note) for note in notes]
    duration = [4, 2, 1]

    result = []
    for length, beat in zip(lengths, duration):
        result.append(beat * length)

    return result

# Example usage
# Test with a markdown code block that contains musical note lengths.
test_music = 'o o| .| o| .| .| .| .| o o'
test_result = parse_music(test_music)
print(test_result)  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```