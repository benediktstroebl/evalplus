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
    result = []

    last_note = None
    for i in range(len(music_string)):
        note = music_string[i]
        if note == last_note:
            result[-1] += 1
        elif note == 'o':
            result.append(1)
        elif note == 'o|':
            result.append(2)
        elif note == '.|':
            result.append(4)
        elif note == 'o.|':
            result.append(3)
        elif note == 'o|o':
            result.append(5)
        elif note == 'o.o':
            result.append(7)
        elif note == 'o|o.|o':
            result.append(8)
        elif note == 'o.o|o.|o':
            result.append(9)
        elif note == 'o.o|o.o.o':
            result.append(11)
        elif note == 'o.o.o|o.o.o':
            result.append(12)
        elif note == 'o.o.o|o.o.o.|o':
            result.append(13)
        elif note == 'o.o.o|o.o.o.o.|o':
            result.append(14)
        elif note == 'o.o.o|o.o.o.o.o.|o':
            result.append(15)
        elif note == 'o.o.o.o.o.o.o.o.|o':
            result.append(16)
        elif note == 'o.o.o.o.o.o.o.o.o':
            result.append(18)
        elif note == 'o.o.o.o.o.o.o.o.o.o':
            result.append(19)
        elif note == 'o.o.o.o.o.o.o.o.o.o.o':
            result.append(20)
        last_note = note
    return result

