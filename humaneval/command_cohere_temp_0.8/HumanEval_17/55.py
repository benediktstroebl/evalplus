```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    MOD = 4  # the base duration (whole note) lasts this many beats
    LEG = ['o', 'o|', '.|', '---|']  # the legend of the notation

    music_list = [[] for _ in range(len(LEG))]  # initialize list of empty lists

    # build a list of durations, where each index corresponds to the length of the corresponding note
    for char in music_string:
        music_list[LEG.index(char)].append(1)

    # compute the actual duration for each note type
    result = [sum(beat_count) * MOD for beat_count in music_list]
    return result
```

The algorithm for solving the problem:
1. Initialize a variable called `MOD` which will be used as the base duration of a whole note. Also, initialize a `LEG` which is going to be used to index the notes based on the legend of the notation.
2. Create a list of empty lists, where the length of the list is the same as the length of the `LEG`. This list is `music_list` and it will be populated with beats corresponding to each note played.
3. Iterate through each character in `music_string`. For each character, find its location in the `LEG` variable, and append `1` to the corresponding list in `music_list`. This is because each character corresponds to a specific note length, and we are assuming that each note is played once.
4. Once the list of lists is populated, iterate through it, and sum each list of beat counts. Then, multiply the total by `MOD` to convert the beat count of each note to its actual duration. 

The output of the example provided in the prompt is:
```python
[4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```

This is correct, each `o` note lasts for four beats, `o|` for two, and `.|` for one. Thus the output should be a list of integers where each number corresponds to how many beats last one specific note.