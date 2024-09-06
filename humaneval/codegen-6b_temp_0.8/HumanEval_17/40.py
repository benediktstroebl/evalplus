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
    music_list = []
    beat = 0
    for i in range(0, len(music_string) - 1):
        if music_string[i] == 'o':
            beat += 1
            if i < len(music_string) - 2:
                if music_string[i + 1] == 'o':
                    beat += 1
                    if i < len(music_string) - 3:
                        if music_string[i + 2] == 'o':
                            beat += 1
                            if i < len(music_string) - 4:
                                if music_string[i + 3] == 'o':
                                    beat += 1
                                    if i < len(music_string) - 5:
                                        if music_string[i + 4] == 'o':
                                            beat += 1
                                            if i < len(music_string) - 6:
                                                if music_string[i + 5] == 'o':
                                                    beat += 1
                                                    if i < len(music_string) - 7:
                                                        if music_string[i + 6] == 'o':
                                                            beat += 1
                                                            if i < len(music_string) - 8:
                                                                if music_string[i + 7] == 'o':
                                                                    beat += 1
                                                                    if i < len(music_string) - 9:
                                                                        if music_string[i + 8] == 'o':
                                                                            beat += 1
                                                                            if i < len(music_string) - 10:
                                                                                if music_string[i + 9] == 'o':
                                                                                    beat += 1
                                                                                    if i < len(music_string) - 11:
                                                                                        if music_string[i + 10] == 'o':
                                                                                            beat += 1
                                                                                            if i < len(music_string) - 12:
                                                                                                if music_string[i + 11] == 'o':
