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

    music_string = music_string.replace(' ', '')
    list_notes = []
    music_length = len(music_string)
    count = 0

    while count < music_length:
        if count + 2 < music_length and music_string[count] == 'o' and music_string[count + 1] == '|':
            list_notes.append(4)
            count += 2
        elif count + 2 < music_length and music_string[count] == 'o' and music_string[count + 1] == '.':
            list_notes.append(2)
            count += 2
        elif count + 2 < music_length and music_string[count] == '.' and music_string[count + 1] == '|':
            list_notes.append(1)
            count += 2
        else:
            count += 1

    return list_notes

