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
    # List of tuples, where each tuple corresponds to a note, and contains duration and position of note in string
    notes = []
    note = ()  # Tuple with duration and position of note
    last_dot_position = 0  # Position of last dot in string

    for i, char in enumerate(music_string):
        if char == 'o':
            note = (4, i)
        elif char == '.':
            last_dot_position = i
        elif char == '|':
            note = (1, last_dot_position)
            notes.append(note)

    return [note[0] for note in notes]

