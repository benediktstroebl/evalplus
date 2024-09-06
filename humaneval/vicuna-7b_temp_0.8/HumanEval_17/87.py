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
        if line.strip() == '':
            beats.append(0)
            continue
        # split line into notes
        notes = line.split('|')
        # remove trailing '.'
        notes = [note for note in notes if note != '.']
        # parse notes
        start, end, note_type = [int(n) if n.isdigit() else None for n in notes]
        if start is None:
            start = end = 1
        beats.append((start, end, note_type))
    return beats

