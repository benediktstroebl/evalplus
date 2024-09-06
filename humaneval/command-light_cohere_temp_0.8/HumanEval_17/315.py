```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = music_string.split('ohow notes are each character that is either 'o', 'o|', '.|' and the last character is the new note.
    notes = [notes[0 if note == 'o' else 4 if note == 'o|' else 1 if note == '.' else 2 if note == '|' else 0]
    return notes

# Test case for function
test_music = '''
o o| .| o| .| .| .| o o
'''
result = parse_music(test_music)
print(result)
```