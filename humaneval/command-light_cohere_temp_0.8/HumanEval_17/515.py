Here's a self-contained Python function that parses and converts a string of musical notes into a list of integers representing the number of beats:
```python
def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,  # whole note
        'o|': 2,  # half note
        '.|': 1  # quarter note
    }
    
    beats = 0
    
    notes_ Found = music_string.split(' ') ')[0].
    for note in notes_Found:
        if note in notes:
            beats += notes[note]
            
    return beats
```

The function takes a string music_string as input and uses a dictionary to map musical notes to the number of beats each one lasts. The function splits the the music_string by ' ', to get all notes, and then loops through the notes to count the number of beats.