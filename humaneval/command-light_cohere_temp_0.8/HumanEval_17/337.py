```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split(" ")". why do we use split(" ") instead of using a separator? Using split(" ") makes the function independent of any potential separators that could be used to create the music_string, which allows for more flexibility. 
For example, it could accept a music_string created by the special text editor, which uses \r (\r represents a carriage return), or even multiple characters that could be used to create a note (although this is less common and would require additional logic to check for valid inputs).

This allows the function to be more flexible and work with any potential inputs. 

The function uses the List[int]() function to convert the string to a list of integers, which are the lengths of each note. This is the solution is a self-contained Python script that solves the problem of parsing a music string into a list of integers representing the number of beats of each note.