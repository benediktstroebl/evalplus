```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = ['o', 'o|', '.|']
    notes_mapping = {note: 4 for note in notes}  # 4 beats for whole note, 2 beats for half note, 1 beat for quarter note

    # Convert string to list of characters
    music_chars = music_string.split()
    particular notes in a list of music_chars
    beats = [notes_mapping.get(note) for note in music_chars]

    return beats

# Test cases
test_data = ['o o| .| o| .| .| .| o o',
              'o o| .| o| .| .| .| o|',
              'oo']

# Call parse_music with test data
result_test = parse_music(test_data)

# Print results
print(result_test)
``` 
This code defines a function `parse_music` that takes a music string in a special format and returns a list of beats. The function uses a legend of notes to map the notes in the string to the number of beats it should last four for whole notes, two for half notes, and one for quarter notes.