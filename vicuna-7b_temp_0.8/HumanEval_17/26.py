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
    for note in music_string:
        # We check for the presence of a trailing '|' character, which is used to indicate that the next
        # note should be shorter than the previous one.
        if note.endswith('|'):
            # We remove the trailing '|' character to get the length of the next note
            note = note[:-1]
        beats.append(int(note))
    return beats

