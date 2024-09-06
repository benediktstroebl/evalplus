```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4, 'o|': 2, '.|': 1
    }
    
    beat_ lengths = {note: notes[0] for note in notes}
    time_signature = music_string[0]
    
    if time_signature != ' ':
        beats = int(time_signature)
        time_signatures = [beats]
    
    notes = [beats] + notes.
    
    music_notes = music_string[1:]
    
    for note in music_token:
        if note in notes:
            beat_lengths[note] += 1
        else:
            beat_lengths[note] = 1
            
        notes.append(beat_lengths[beat])
        
    return notes
```