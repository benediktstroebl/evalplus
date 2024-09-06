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

    # Your solution here

    # input string
    # split by |
    # get list of notes
    # create a mapping dictionary
    # - 'o': 4
    # - 'o|': 2
    # - '.': 1
    # append number of beats to the list of notes
    # return the list

    notes = music_string.split('|')
    notes_length = {
        'o': 4,
        'o|': 2,
        '.': 1
    }

    parsed_notes = []
    for note in notes:
        note_length = notes_length.get(note[0])
        if note_length is None:
            raise ValueError(f'Invalid note {note}')

        note_length *= len(note)
        parsed_notes.append(note_length)

    return parsed_notes

