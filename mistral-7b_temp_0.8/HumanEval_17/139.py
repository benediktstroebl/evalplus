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

    # 1) Remove all the chars that are not in the "o, |, ., " format
    #    hint: use the translate() method on the string to remove unwanted chars
    #    https://www.w3schools.com/python/ref_string_translate.asp

    # 2) Make sure that all your musical notes are separated by a space, so you can split the string into an
    #    array of musical notes.

    # 3) Convert the musical notes into integers by using the mapping:
    #     'o' - 4
    #     'o|' - 2
    #     '.|' - 1
    #    Use the map() function to do this conversion:
    #    https://www.w3schools.com/python/ref_func_map.asp

    # 4) Return the converted list of musical notes.

    return list(map(lambda x: 4 if x == 'o' else 2 if x == 'o|' else 1, music_string.translate(str.maketrans('',
