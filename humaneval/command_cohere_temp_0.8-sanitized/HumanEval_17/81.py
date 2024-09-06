from typing import List
pattern = '^ *([o|.|}]*) *$'
def parse_music(music_string: str) -> List[int]:
    """ Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return list of integers corresponding to how many beats does each
    not last.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    >>> parse_music('o o| .| o| o| .| .| .| .| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    if not re.match(pattern, music_string):
        raise ValueError('Invalid music string')

    beats = []
    note = 4
    for char in music_string.strip():
        if char == 'o':
            beats.append(note)
        elif char == '|':
            note -= 2
        elif char == '.':
            note -= 1
        else:
            raise ValueError('Invalid character in music string')

    return beats