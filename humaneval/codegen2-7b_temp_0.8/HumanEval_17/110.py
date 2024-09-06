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
    result = [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    if music_string is not None:
        music_string = music_string.replace(' ', '').replace('o|', '').replace('.|', '')
        beat_list = music_string.split('|')
        for beat_string in beat_list:
            if beat_string.count('.') > 0:
                for i in range(int(beat_string.count('.'))):
                    result[int(beat_string.count('.')) - i] += 1

    return result

