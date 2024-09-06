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
    beat_duration = [4, 2, 1]
    music_string = music_string.replace('|', '')
    if music_string.count('o') > 0:
        return [4 for i in music_string]

    notes = [beat_duration[music_string[i].index('o')] for i in range(len(music_string))]
    return notes

