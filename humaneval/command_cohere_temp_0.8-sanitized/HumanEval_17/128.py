import re
from typing import List
def parse_music(music_string: str) -> List[int]:
    # Regular expression to match a pattern in music string
    pattern = re.compile(r'o|' +
                        r'(?P<len>.)\|' +
                        r'(?P<len1>.)|' +
                        r'(?P<len2>.)\.' +
                        r'*')

    # Example string with some beats marked
    example_string = 'o o| .| o| o| .| .| .| .| o o'

    # Getting total number of beats and splitting the string into separate beats
    beats_number = len(example_string) // 4
    beats_string = example_string[:beats_number*4]

    # Finding all the matches of the pattern in the beats string
    matches = pattern.findall(beats_string)

    # Initialising the output list
    result = []

    # Counting the beats length for each match
    for match in matches:
        result.append(len(match))

    # Returning the result
    return result