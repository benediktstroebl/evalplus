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
    notes = [0] * (len(music_string) + 1)

    for i in range(1, len(music_string)):
        if music_string[i - 1] == 'o' and music_string[i] == 'o':
            notes[i] = notes[i - 1] + 1
        elif music_string[i - 1] == 'o':
            notes[i] = notes[i - 1] + 2
        elif music_string[i] == 'o':
            notes[i] = notes[i - 1] + 1
        elif music_string[i - 1] == 'o' and music_string[i] == 'o|':
            notes[i] = notes[i - 1] + 1
        elif music_string[i - 1] == 'o' and music_string[i] == '.|':
            notes[i] = notes[i - 1] + 0.5
        elif music_string[i - 1] == 'o' and music_string[i] == 'o|':
            notes[i] = notes[i - 1] + 0.5
        elif music_string[i - 1] == 'o' and music_string[i] == '.|':
            notes[i] = notes[i - 1] + 0.5
        elif music_string[i - 1] == 'o' and music_string[i] == '.|':
            notes[i] = notes[i - 1] + 0.5
        elif music_string[i - 1] == 'o' and music_string[i] == 'o':
            notes[i] = notes[i - 1] + 0.5
        elif music_string[i - 1] == 'o' and music_string[i] == 'o|':
            notes[i] = notes[i - 1] + 0.5
        elif music_string[i - 1] == 'o' and music_string[i] == '.|':
            notes[i] = notes[i - 1] + 0.5

    return notes[len(music_string) - 1]

