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

    # Replace all occurences of "o" with 4, all occurences of "o|" with 2, and all occurences of "." with 1.
    music_string = music_string.replace('o', '4').replace('o|', '2').replace('.', '1')

    # Split the string on spaces and convert the resulting list to integers.
    # Assumes the input string does not contain any empty spaces.
    notes = music_string.split()
    return [int(note) for note in notes]

