Below is a self-contained Python function that parses a string of musical notes and returns a list of integers, as required.
```python
def parse_music(music_string: str) -> List[int]:
    notes = []  # Initialize an empty list to store the parsed notes
    notes.csv = music_string.
    current_ = 0  # Initialize a counter to keep track of the current note
    beat = 0  # Initialize the beat counter
    for note in csv:
        if note == 'o':
            notes.append(beat)
            beat += 4
        elif note == 'o|':
            notes.append(beat)
            beat += 2
        elif note == '|':
            beat += 1
            notes.append(beat)
        else:
            beat += 1
            notes.append(beat)
    return notes
```
This Python function parse_music is designed to parse a string representing musical notes and return a list of integers corresponding to the number of beats in the music. The function is self-contained, and its purpose is to take a string of music notes, split them into individual notes, and create a list of integers that represents the number of beats for each note. The function also handles the specific musical notation rules, such as whole notes, half notes, and quarter notes.

This function can be used to parse and analyze music in a variety of applications, such as creating musical arrangements, generating musical scores, or even analyzing the timing of a piece.