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
    # Base case: an empty string
    if music_string == "":
        return []

    # Recursive case: we can use the following properties of the string
    # * the first character is a whole note if it's 'o', a half note if it's 'o|' or a quarter note if it's '.|'
    # * the rest of the string doesn't contain a whole note
    if music_string[0] == "o":
        return [4] + parse_music(music_string[1:])
    elif music_string[0] == "o|":
        return [2] + parse_music(music_string[2:])
    elif music_string[0] == ".|":
        return [1] + parse_music(music_string[2:])

