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
    # Strip leading and trailing whitespaces.
    cleaned = music_string.strip()

    # Store parsed notes in a list.
    parsed = []

    # Loop through all characters.
    for char in cleaned:
        # If 'o' input, add '4' to the list.
        if char == 'o':
            parsed.append(4)

        # If 'o|' input, add '2' to the list.
        elif char == 'o|':
            parsed.append(2)

        # If '.|' input, add '1' to the list.
        elif char == '.|':
            parsed.append(1)

    # Return the list of parsed notes.
    return parsed

