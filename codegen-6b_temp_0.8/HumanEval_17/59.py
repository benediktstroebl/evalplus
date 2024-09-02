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
    music_list = [0] * (len(music_string)*4)
    index = 0
    for note in music_string:
        if note != 'o':
            song = note
        elif note == 'o':
            if index % 4 == 0:
                song = 'o'
            elif index % 4 == 1:
                song = '.|'
            elif index % 4 == 2:
                song = ' o|'
            else:
                song = '.|'
        index += 1
        if note == 'o':
            if song == 'o':
                music_list[index - 1] = 4
            elif song == '.|':
                music_list[index - 1] = 2
            elif song == ' o|':
                music_list[index - 1] = 1
    return music_list

