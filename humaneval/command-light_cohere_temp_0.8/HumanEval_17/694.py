```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    beats = music_string.split(' '|')
    notes.
    output = []
    beats[0].append(notes[0])
    for i in range(1, len(beats)-1):
        current_beat = beats[i]
        next_beat = beats[i+1]
        output.append(notes[current_beat] * (notes[next_beat] - notes[current_beat]) // (notes[next_beat] - notes[current_beat] + 2))
        output.append(current_beat)
    return output
``` 
This code defines a function that parses a music notation string. It uses a code splitting to separate the beats and then uses a dictionary to map the musical notes to the number of beats they represent. The function then concatenates the beats to the output array, where each element is the number of beats corresponding to the current beat, with the note for the next beat subtracted, and wraps around by adding the beat to the output.

The function then returns a list of integers corresponding to the number of beats in each musical note.