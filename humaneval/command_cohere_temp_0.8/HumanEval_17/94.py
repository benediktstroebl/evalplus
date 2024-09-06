```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    beat_mapping = {'o': 4, 'o|': 2, '.': 1}
    notes = []
    curr_beat = 0
    
    for char in music_string:
        if char in beat_mapping:
            curr_beat += beat_mapping[char]
            notes.append(curr_beat)
        else:
            # If we encounter an invalid input, skip it and continue with the next character
            continue
    
    return notes
```

The Python script provides a function called `parse_music` that takes a string input formatted according to a given notation specification. This specification details that 'o' represents a whole note with four beats, 'o|' represents a half note with two beats, and '.|' represents a quarter note with one beat. The function's purpose is to extract beat information from the input string and transform it into an array of integers that denote the duration of each note in terms of beats.

The beat mapping is initiated as a dictionary to provide a mapping between each notation character and its corresponding beat value. The function initializes an empty list called `notes` where the extracted beat values for each note will be stored. Additionally, `curr_beat` is initialized to 0, which is later incremented with the beat values as relevant characters are encountered.

The function iterates over the input string character by character. Whenever it encounters a character that is included in the beat mapping dictionary, it adds the corresponding beat value to the `curr_beat` variable. Afterward, it appends this updated `curr_beat` value to the notes list. However, if an unsupported character is encountered, the function continues to process the string by skipping past that character.

By the time the function concludes processing the input string, the `notes` list will comprise integers that indicate the number of beats for each corresponding note.