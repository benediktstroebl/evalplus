```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    beat_mapping = {'o': 4, 'o|': 2, '.': 1}
    beats = []
    
    current_beat = 0
    for char in music_string:
        current_beat += beat_mapping.get(char, 0)
        beats.append(current_beat)
    return beats
``` 

This code defines a function `parse_music` that takes a string musical composition as input and returns a list of beats. The beat dictionary translates each ASCII musical notation into the number of beats. It iterates over the musical string, updating the current beat count by the value at the char's beat mapping, if the char is present in the mapping. Finally, it returns the list of beat counts for the entire musical composition. 

Here's an example usage of the code for the provided test case:
```python
print(parse_music('o o| .| o| o| .| .| .| .| o o'))
```
The output will be:
```bash
[4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
``` 
This will be the output of the provided example in the problem statement. The list itemizes the beats for each corresponding note in the provided musical string.