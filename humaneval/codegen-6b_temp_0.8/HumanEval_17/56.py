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
    # [0] is a dummy for iterations purposes
    parsed_music_list = [0 for i in range(len(music_string))]
    for i in range(len(music_string)):
        if music_string[i] == 'o':
            parsed_music_list[i] = 4
        elif music_string[i] == 'o|':
            parsed_music_list[i] = 2
        elif music_string[i] == 'o|o':
            parsed_music_list[i] = 1
        elif music_string[i] == 'o|o|':
            parsed_music_list[i] = 0
        elif music_string[i] == 'o|o|o':
            parsed_music_list[i] = -1
        elif music_string[i] == 'o|o|o|':
            parsed_music_list[i] = -2
        elif music_string[i] == 'o|o|o|o':
            parsed_music_list[i] = -3
        elif music_string[i] == 'o|o|o|o|':
            parsed_music_list[i] = -4
        elif music_string[i] == 'o|o|o|o|o':
            parsed_music_list[i] = -5
        elif music_string[i] == 'o|o|o|o|o|':
            parsed_music_list[i] = -6
        else:
            print(f'Unknown note: {music_string[i]}')
    return parsed_music_list
    
