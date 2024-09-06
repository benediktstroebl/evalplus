from typing import List
def parse_music(music_string: str) -> List[int]:
    """ Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return a list of integers corresponding to how many beats does each
    note last.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    Args:
        music_string (str): Musical string to parse

    Returns:
        List[int]: Beats for each parsed note

    >>> parse_music('o o| .| o| o| .| .| .| .| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    RES_DICT = {
        'o': 4,
        'o|': 2,
        '.|': 1,
    }

    return [RES_DICT[curr] for curr in music_string if curr in RES_DICT]