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
    beats_per_note = {
        "o": 4,
        "o|": 2,
        ".": 1
    }

    # TODO: Implement this function
    music_list = []
    for char in music_string:
        if char == "o" or char == "o|":
            music_list.append(beats_per_note[char])
        elif char == ".":
            music_list.append(beats_per_note[char])
        else:
            raise ValueError("Wrong input")
    return music_list

