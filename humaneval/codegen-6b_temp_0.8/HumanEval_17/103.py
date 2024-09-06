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
    result = []
    parts = music_string.split('o ')
    for part in parts:
        # print(part)
        chunks = part.split(' ')
        # print(chunks)
        count = 0
        for chunk in chunks:
            # print(chunk)
            if chunk == '.|':
                count += 1
            elif chunk == 'o|':
                count += 2
            elif chunk == '.|':
                count += 1
        result.extend([count for _ in range(count)])
        # print(str(count) + ' ' + str(result))
    return result

