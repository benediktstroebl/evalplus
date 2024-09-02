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
    result = []
    for line in music_string.split('\n'):
        # skip empty lines
        if not line:
            continue
        # split the line into a sequence of notes
        notes = line.split('|')
        # parse each note
        for note in notes:
            # convert the note to an integer
            if note == 'o':
                # whole note
                note = 4
            elif note == 'o|':
                # half note
                note = 2
            elif note == '.|':
                # quarter note
                note = 1
            # add the note to the result list
            result.append(note)
    return result