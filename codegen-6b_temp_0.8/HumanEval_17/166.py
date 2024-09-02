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
    # Split music_string into (note, rest) tuples
    parsed = [(note, rest) for note, rest in zip(music_string.split('o'), music_string.split('o|'))]
    # The rest of the tuples are all pairs of (note, rest)
    parsed = parsed[:-1] + [(note, rest) for note, rest in zip(parsed[-1][0], parsed[-1][1])]

    # Create beats list
    beats = []
    for note, rest in parsed:
        if note == 'o':
            beats.append(1)
        elif note == 'o|':
            beats.append(0.5)
        elif note == '.':
            beats.append(0.25)

    return beats

