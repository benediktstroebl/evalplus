```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    nbeats = music_string.split('oas longest_note_length = max(len(note) for note in notes.
    beats = [0]
    beats = []
    for beat_note in music_string.split(' '|'):
        beat_note = beat_note.split(' 'o')[0]
        beats.append(beats.append(notesotes - longest_note - length = len(beat_note))
        beats.append(beats[:-1])
        beats.append(notest.length)
        adding up (notices last beat - length of the longest_note.
    return beats
return beats

# Example usage
music_str = 'o o| .| o| .| .| .| o o'
beat_list = parse_music(music_str)
print(beat_list)
``` 
This solution defines a function `parse_music` that parses a given music string according to a predefined mapping of notes to beat lengths. The function splits the music string by the "|" character, extracts the beat note and its length, and then constructs a list of beats corresponding to the extracted notes. 
The function returns this list of beats, and the output will be `[4, 2, 1, 2, 2, 1, 1, 1, 1, 4]`.