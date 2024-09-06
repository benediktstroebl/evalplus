```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1}
    beats = music_string.split(' '|')
   
    beat_count = [int(beat) for beat in beats.
    return [beat_count]

# Test cases
music_cases = [
    "o o| .| o| .| .| .| .| o o",
    "o o| o| .| o| .| .| .| .",
    "oo",
]

test_results = []
for music in music_cases:
    try:
        beats = parse_music(music)
        test_results.append(beats)
    except Exception as e:
        print(f"Error in {music}: {e}")

print("Test Results:")
for result in test_results:
    print(result)
```