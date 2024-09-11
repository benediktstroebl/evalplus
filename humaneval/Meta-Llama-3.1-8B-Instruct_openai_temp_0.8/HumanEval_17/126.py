### Music Note Parser

Below is a Python script that solves the problem:

```markdown
### Music Note Parser

This script takes a string representing musical notes in a special ASCII format, 
parses it, and returns a list of integers corresponding to how many beats each note lasts.

### Code

```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format.

    Args:
    music_string (str): A string representing musical notes.

    Returns:
    List[int]: A list of integers corresponding to how many beats each note lasts.
    """
    notes = music_string.split()
    durations = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    
    # Initialize an empty list to store the durations of notes
    parsed_music = []
    
    # Iterate over each note in the music string
    for note in notes:
        # Append the duration of the current note to the parsed music list
        parsed_music.append(durations.get(note, 0))
    
    return parsed_music

### Example Usage

if __name__ == "__main__":
    music_string = 'o o|.| o| o|.|..|..|. o o'
    parsed_music = parse_music(music_string)
    print(parsed_music)
```

### Explanation

The script defines a function `parse_music` that takes a string of musical notes as input, 
parses it, and returns a list of integers corresponding to how many beats each note lasts.

 Inside the function, it first splits the input string into a list of individual notes. 
It then defines a dictionary `durations` that maps each note to its duration in beats.

The script then iterates over each note in the list, looks up its duration in the `durations` dictionary, 
and appends it to the `parsed_music` list.

Finally, the script includes an example usage of the `parse_music` function with a sample input string.

### Running the Script

Save the script to a file (e.g., `music_parser.py`) and run it using Python (e.g., `python music_parser.py`). 
The script will print the parsed music list for the sample input string.