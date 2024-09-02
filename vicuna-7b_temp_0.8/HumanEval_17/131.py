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
        # This function will only work for lines that have two notes
        if len(line) < 4:
            continue
        # Split the line into two notes
        notes = line.split('|')
        # Parse the notes
        beats.append(int(notes[0]))
        beats.append(int(notes[1]))
    return beats
