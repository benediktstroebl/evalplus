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

    pattern = re.compile(r'([oo]+|([oO]+|\.\s*[oO]+|\s*\.\s*[oO]+)*)\s*(\d+)')
    results = []

    for match in pattern.finditer(music_string):
        start, end, duration = match.groups()
        results.append(int(duration.strip()))

    return results

