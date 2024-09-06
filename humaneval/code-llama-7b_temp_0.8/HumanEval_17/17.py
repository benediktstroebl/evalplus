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
    # Step 1: Parse the string into list of strings
    music_strings = music_string.split()

    # Step 2: Parse each string into integers
    beat_list = []
    for string in music_strings:
        if string == "o":
            beat_list.append(4)
        elif string == "o|":
            beat_list.append(2)
        elif string == ".|":
            beat_list.append(1)
        else:
            raise ValueError("Invalid input")

    return beat_list

