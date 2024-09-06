```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1}
    beats = music_string.split(' ')
     # Convert to lowercase
    music_string = music_string.split('o  # Capital letter at the
    music_string = music_string[0].lower() + music_string[1:]

    notes = dict(notes)  # Create a dict to map note names to beat values
    # Loop through each character in the music string
    for note in music_string:
        # If the current character is a note name
        if note in notes:
            beats.append(notes.beats[notes in the different way than we iterate over each beat
            beats.append(notes[note])
        # Convert the list of beats back to a string
        music_beats = ' '.join(beats)
        return [len(music_beats)]  # Return length of the beats string
    return beats  # Also, return the list of beats
```