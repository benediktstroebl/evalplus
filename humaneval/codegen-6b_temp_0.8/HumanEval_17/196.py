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
    current_note = ''
    for index, note in enumerate(music_string):
        if note == ' ':
            result.append(1)
        elif note == 'o':
            result.append(4)
        elif note == 'o|':
            result.append(2)
        elif note == '.':
            result.append(1)
        elif note == '|':
            result.append(4)

        current_note += note

        if index == len(music_string)-1:
            result.append(1)
        elif index == len(music_string)-2:
            if current_note == 'o|o':
                result.append(2)
            else:
                result.append(1)
        elif index == len(music_string)-3:
            if current_note == 'o|o|':
                result.append(2)
            else:
                result.append(1)

    return result

