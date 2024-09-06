from typing import List
PATTERN = "^ *([o|.|]) *(?: *[o|.|])* *$"
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
    if not music_string.strip().lower().match(PATTERN):
        raise ValueError("Invalid music string. Expected format:")
    notes = music_string.strip().lower()
    return [4 if c == 'o' else 2 if c == 'o|' else 1 for c in notes]