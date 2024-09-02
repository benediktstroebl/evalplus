from typing import List


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
    music_symbols = [
        ['o', 'o|'],
        ['.|']
    ]
    music_symbols = [symbol for sublist in music_symbols for symbol in sublist]
    list_of_music = music_string.split()
    return list(
        map(lambda music_symbol: 1 if music_symbol == '.' | 2 if music_symbol == 'o' | 4 if music_symbol == 'o|'
            else 0, list_of_music)
    )

