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
    beats = [0] * 12
    pattern = r'([oO][a-z]+|[0-9]+)'

    for note in music_string.split('|'):
        match = re.search(pattern, note)
        if match:
            duration, note_type = match.groups
            if note_type == 'o':
                beats[int(duration) - 1] += 1
            else:
                beats[int(note_type) - 1] += 1

    return beats