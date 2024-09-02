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
    cur_notes = 0
    cur_note = music_string[0]
    for c in music_string[1:]:
        if 'o' == cur_note and 'o' == c:
            cur_notes += 1
        elif 'o' == cur_note and 'o' != c:
            cur_notes = 1
        elif 'o' != cur_note and 'o' == c:
            result.append(cur_notes)
            cur_notes = 1
        elif 'o' != cur_note and 'o' != c:
            cur_notes = 0
        elif '.' == cur_note and '.' == c:
            pass
        elif '.' == cur_note and '.' != c:
            cur_notes += 1
        elif '.' != cur_note and '.' == c:
            cur_notes -= 1
            
        cur_note = c
    result.append(cur_notes)
    return result
    pass

