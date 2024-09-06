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
    parsed = []
    current_note = ""
    for c in music_string:
        if c == "o":
            parsed.append(4)
            current_note += c
        elif c == "o" or c == ".":
            parsed.append(1)
            current_note += c
        elif c == "|" and current_note!= "":
            parsed.append(1)
            current_note += c
        elif c == "|" and current_note == "":
            current_note += c
    return parsed

