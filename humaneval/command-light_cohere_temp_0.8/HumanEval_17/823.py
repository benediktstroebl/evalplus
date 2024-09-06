Here's a self-contained Python function that parses a music string containing musical notes represented in ASCII format and returns a list of integers representing the duration of each note in beats:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of music in a specific ASCII format, 
    representing notes and their durations. 
    The task is to parse this string and return a list of integers corresponding to the duration of each note in beats. 
    The input format is a string of the form '1234|nm|1234...', where nm is a note name, 
    and 1234 is the duration of the note in beats.
    """
    function is designed to handle the following input format:
    '1234|nm|1234...', where nm is a note name and 1234 is the duration of the note in beats. 
    """
    function returns a input string music_string and returns a list of integers. The function uses the string to split the notes using the pipe character '|' to get the note name and the duration. The note is then split into a list of strings, which are then converted into a list of integers representing the duration of each note in beats.

Here is a test code for this function:
```python
parse_music('1234|mol|1234...')
```