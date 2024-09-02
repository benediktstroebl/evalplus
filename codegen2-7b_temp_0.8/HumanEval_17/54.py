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
    parsed = [0] * len(music_string)
    counter = 0
    for index in range(len(music_string)):
        if music_string[index] == "o":
            if index!= counter:
                parsed[index] = parsed[index] + (4 - (counter - index))
            counter += 1
        elif music_string[index] == "o|":
            if index!= counter:
                parsed[index] = parsed[index] + (2 - (counter - index))
            counter += 2
        elif music_string[index] == ".":
            counter += 1
    
