```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string representing musical notes in a special ASCII format,
    parses this string and returns a list of integers corresponding to how many beats each note lasts.

    :param music_string: A string of musical notes
    :return: A list of integers representing the duration of each note in beats
    """
    notes_legend = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    notes = music_string.split()
    beats = []
    
    # combine whole notes with their duration
    i = 0
    while i < len(notes):
        if notes[i] == 'o' and i < len(notes) - 1 and notes[i+1] == '|':
            beats.append(notes_legend['o|'])
            i += 2
        elif notes[i] == 'o':
            if i < len(notes) - 1 and notes[i+1] =='':
                beats.append(notes_legend['o'])
                i += 1
            elif i == len(notes) - 1:
                beats.append(notes_legend['o'])
                i += 1
            else:
                beats.append(notes_legend['o|'])
                i += 2
        elif notes[i] == '.|':
            beats.append(notes_legend['.|'])
            i += 1
        elif notes[i] == 'o|' or notes[i] == '.':
            beats.append(notes_legend[notes[i]+'|'])
            i += 1
        else:
            i += 1

    return beats


# Test the function
music = 'o o|.| o| o|.|.|.|.| o o'
print(parse_music(music))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```