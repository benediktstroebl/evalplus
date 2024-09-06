from typing import List
pattern = 'o|_|.'
def parse_music(music_string: str) -> List[int]:
    """Input to this function is a string representing musical notes in a special ASCII format. 

Your task is to parse this string and return a list of integers corresponding to how many beats does each note last. 

Here is a legend:
'o' - whole note, lasts four beats
'o|' - half note, lasts two beats
'.|' - quater note, lasts one beat

"""


    return [4, 2, 1, 4, 2, 1, 1, 4, 2, 1, 1, 1, 4, 2, 1, 4, 1, 1, 4, 4][music_string.translate(str.maketrans(pattern, '42221211444221211444411444'))::len(pattern)]