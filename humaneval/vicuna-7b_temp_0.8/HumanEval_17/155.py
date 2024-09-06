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
    beats = 0
    for note in music_string.split('\n'):
        if note == '':
            continue

        if note[0] == '>':
            # This is a time signature change.
            # We store the number of beats per measure as a string
            # and then parse it using slicing
            num_beats = int(note[2:].split(':')[0])
            beats_per_measure = int(note[2:].split(':')[1])
            beats = (num_beats * beats_per_measure) % 4

        # If the note is not a time signature change,
        # we parse it as follows:
        # - If the note is 'o', it represents a whole note
        # - If the note is 'o|', it represents a half note
        # - If the note is '.|', it represents a quarter note
        if note == 'o':
            beats += 1
        elif note == 'o|':
            beats += 2
        elif note == '.|':
            beats += 1

    return beats