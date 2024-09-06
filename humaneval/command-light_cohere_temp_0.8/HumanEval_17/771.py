```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = ['o', 'o|', '|', 'o', '.', '|', '.', 'o']
    beat_counts = {note: 4 for note in notes}
    stave = [''] + ['o'] * 4 + ['o'] * 4 + ['']
    result = [beat_counts[x] for x in music_string.assertator and list(stave) + ['']]
    return result
``` 
The parse_music function takes a music_string parameter that represents a sequence of notes, and returns a list of integers representing the number of beats for each note. The function uses a legend and a dictionary to map the notes to the number of beats they last. The function then creates a stave of musical notes and a space, then iterates through the music_string and adds the number of beats for each note to the result list.