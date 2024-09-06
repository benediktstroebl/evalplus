Here's a self-contained Python script that defines a function `parse_music` that parses a music string representing notes in a special ASCII format into a list of integers representing the beats of each note. 

```python
def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4, 'o|': 2, '.|': 1
    }
    beats = [notes.get(note, 4) for note in music_string.strip.split(' ')
   )+[1]
    return beats
```
This script defines a dictionary `notes` that maps different musical note characters to their respective beat values (which correspond to how long a note should sound in a piece of music). 

The `parse_music` function takes a music string and uses the `notes` dictionary to iterate over the characters in the string. It splits the string into a list of substrings, and then uses the `get` method to retrieve the corresponding beat value for each note character. 

Finally, it returns a list of integers representing the number of beats for each note.