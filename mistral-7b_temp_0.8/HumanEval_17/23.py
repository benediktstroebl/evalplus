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
    beat_len = [1, 2, 4]
    parsed_list = []
    beat_num = 0
    for item in music_string:
        if item == "|":
            beat_num += 1
        elif item == "o":
            parsed_list.append(beat_len[beat_num - 1])
        else:
            continue

    return parsed_list

