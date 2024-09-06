```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1}
    time_signature = music_string[0]
    
    if time_signature != 'o o| .| o| .| .| .| .| o':
        raise ValueError("Invalid time signature")
        
    beats = len(music_string) - 1
    beat_numbers = []
    for i in range(beats):
        note_start = i * 4 if time_signature == 'o o| .| else i * 2
        note_end = note_start + 1 if time_signature == 'o o|.' else note_start
        
        if note_start not in notes or note_end <= len(music_string) - 1:
            raise ValueError("Invalid note duration")
        
        note = int(music_string[note_start:note_end])
        beat_numbers.append(note)
        
    return beat_numbers

def test_parse_music():
    music_str = "o o| .| o| .| .| .| .| o o"
    beats = parse_music(music_str)
    print(beats)

# Example usage
test_parse_music()
```

This code defines a `parse_music` function that takes a music string in a special ASCII format, parses it and returns a list of integers representing the number of beats in each note.

The function first checks if the time signature is correct and then uses this information to extract the beat information from the music string.  The tests the function by providing a music string and expecting it to correctly parse the beats.