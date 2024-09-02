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
    temp_string = ''
    total_time = 0
    time = 0
    time_len = 0
    time_type = None
    i = 0
    lst = []
    while i < len(music_string):
        if (len(music_string) - i) % 4 == 0:
            temp_string += music_string[i]
            i += 1
        if music_string[i] == 'o':
            temp_string += music_string[i]
            i += 1
            if i < len(music_string):
                if music_string[i] == 'o' or music_string[i] == 'o|':
                    time_type = "whole" if music_string[i] == 'o' else "half"
                    time_len = 2
                    i += 1
                    time += 4
                    total_time += 4
                elif music_string[i] == 'o':
                    time_type = "whole"
                    time_len = 1
                    time += 2
                    total_time += 2
                else:
                    time += 1
                    total_time += 1
            else:
                time += 1
                total_time += 1
        elif music_string[i] == '.':
            temp_string += music_string[i]
            i += 1
            if i < len(music_string):
                if music_string[i] == 'o' or music_string[i] == 'o|':
                    time_type = "whole" if music_string[i] == 'o' else "half"
                    time_len = 0.5
                    i += 1
                    time += 1
                    total_time += 1
                else:
                    time += 0.5
                    total_time += 0.5
            else:
                time += 0.5
                total_time += 0.5
        elif music_string[i] == '|':
            temp_string += music_string[i]
            i += 1
            if i < len(music_string):
                if music_string[i] == 'o' or music_string[i] == 'o|':
                    time_type = "wh