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
    beats = []
    for line in music_string.split('\n'):
        # Split the line into notes
        notes = line.split()
        # Parse the notes
        for i, note in enumerate(notes):
            # Check if the note is the last note of the measure
            if i == len(notes) - 1:
                # If it is, add 4 beats to the current beat count
                beats.append(4)
            else:
                # If it is not, add 1 beat to the current beat count
                beats.append(1)
    return beats

