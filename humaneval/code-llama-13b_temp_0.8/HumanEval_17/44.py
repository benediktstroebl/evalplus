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
    # The naive approach is to use a for loop and if/elif/else statements
    # The more elegant approach is to use a dictionary
    # Lets go with the dictionary approach
    # We need to use a lambda function to convert the key into the corresponding value
    # The code is more elegant, and less error prone
    # We'll use this approach in the other functions
    note_dict = {
        'o': lambda beat: 4 * beat,
        'o|': lambda beat: 2 * beat,
        '.|': lambda beat: beat
    }
    return [note_dict[note](1) for note in music_string.split()]

