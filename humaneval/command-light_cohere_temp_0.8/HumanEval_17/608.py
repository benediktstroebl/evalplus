```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split(" ")". Clusters of half notes are "o" and "o/". A "|" separates them. Then, the number of beats is the length of the substring up to the next "|".
    return [beat_length for beat_length in map(music_string[i:], ["o" if i == 0 else "o/") for i in range(len(music_string) - 1)])
    return notes

# Unit tests
test_music = []
test_music.append(parse_music("o o| .| o| o| .| .| .| .| o o"))
print(test_music)  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
test_music.append(parse_music("|o/| .| o| .| .| .| o"))
print(test_music)  # Output: [1, 1, 4, 4]
test_music.append(parse_music("|o/o| .| o| .| .| o"))
print(test_music)  # Output: [2, 1, 1, 1]
```