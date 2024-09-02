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
    music_list = music_string.split(' ')
    music_list = [music_part for music_part in music_list if music_part]
    music_list = [music_part.split('|') for music_part in music_list]
    music_list = [item[0] if not item[1:] else item[1] for sublist in music_list for item in sublist]
    return [4 if music_note == 'o' else 1 for music_note in music_list]

