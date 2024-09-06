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
    midi_dict = {'a': 33, 'b': 34, 'c': 35, 'd': 36, 'e': 37, 'f': 38, 'g': 39, 'h': 40, 'i': 41, 'j': 42,
                 'k': 43, 'l': 44, 'm': 45, 'n': 46, 'o': 47, 'p': 48, 'q': 49, 'r': 50, 's': 51, 't': 52,
                 'u': 53, 'v': 54, 'w': 55, 'x': 56, 'y': 57, 'z': 58, '1': 59, '2': 60, '3': 61, '4': 62,
                 '5': 63, '6': 64, '7': 65, '8': 66, '9': 67, '0': 68, '|': 69, '_': 70}

    return [len(song) for song in music_string.split('o')]

