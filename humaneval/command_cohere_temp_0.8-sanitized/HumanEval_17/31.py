from typing import List
PATTERN = "/(?P<whole>o)(?P<half>o|)|(?P<quarter>.)/"
def parse_music(music_string: str) -> List[int]:
    """Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return list of integers corresponding to how many beats does each
    note last.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    >>> parse_music('o o| .| o| o| .| .| .| .| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    result = []
    for match in re.finditer(PATTERN, music_string):
        whole = match.group("whole")
        half = match.group("half")
        quarter = match.group("quarter")
        result.extend([4 if whole else 2 if half else 1 for _ in range(len(whole or half or quarter))])
    return result