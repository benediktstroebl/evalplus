```python
from typing import List

 Pattern = str


def parse_music(music_string: Pattern) -> List[int]:
    """Input to this function is a string representing musical notes in a special ASCII format. 

Your task is to parse this string and return list of integers corresponding to how many beats does each
note last.

Here is a legend:
'o' - whole note, lasts four beats
'o|' - half note, lasts two beats
'.|' - quater note, lasts one beat

"""

# Defines regex pattern to find the tempo of each beat
note = r'(?P<whole>o)|(?P<half>o\|)|(?P<quarter>.\|)'

# Defines a regex pattern to find multiple beats with any combination
combination = r'{}{}{}'.format(note, optional note, optional note)

beats = []

for match in re.finditer(combination, music_string):
    beat = match.group()
    if beat.find('o') != -1:
        beats.append(4)
    elif beat.find('o|') != -1:
        beats.append(2)
    else:
        beats.append(1)

return beats
```

The script utilizes the `re` (regular expressions) module to parse the musical string. It defines a pattern
for the beats, which can be whole, half, or quarter notes, and a pattern for combinations of beats,
which are followed by optional beats. 

The list of beats is initialized empty, and in the `for` loop, each combination of beats is found using the
combination pattern. Then, the appropriate value is appended to the list based on the beat found.

The `parse_music` function returns the list of beats, each beat corresponding to its duration. 

This approach allows for flexible and efficient parsing of the musical string, providing a list of integers
representing the beat durations. 
```