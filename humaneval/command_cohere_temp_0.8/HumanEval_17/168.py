```python
from typing import List

pattern = 'o|_|.'

def parse_music(music_string: str) -> List[int]:
    Beats = ['o', '|', '.']
    result = []
    
    for i in range(len(music_string)):
        if music_string[i] in pattern:
            result.append(Beats.index(music_string[i]))
    
    return result
``` 

The algorithm of the parsing function goes as follows:
1. Getting the `music_string` input from the user.
2. Creating a pattern named `Beats` and filling it with the special symbols from the problem statement in corresponding order.
3. Creating an empty list named `result` to store the final result, which is the number of beats for each music symbol.
4. Running a loop to iterate over the music string and assigning the index of found symbol in the `Beats` array to the `result` list.
5. Returning the resulting list. 

The `Beats.index(music_string[i])` method is used for finding the index of the symbol in the beats array, and the existence of the `Beats` array makes the code independent from the actual symbols and their meanings. The code is compact and easy to understand, using basic Python data structures and methods. 

Note that the function assumes that the input will contain only the symbols listed in the `pattern` variable, and may fail or give incorrect results for other input strings. You can improve this by adding error handling to check that all input characters are valid notes, and provide feedback to the user if they are not.