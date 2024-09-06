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
    def parse_note(note: str) -> int:
        if note[0] == 'o':
            return 4
        if note[1] == '|':
            return 2
        return 1

    if len(music_string) % 3!= 0:
        raise ValueError('input music string has to be a multiple of 3')

    music_list = [parse_note(note) for note in music_string.split(' ')]
    return music_list

