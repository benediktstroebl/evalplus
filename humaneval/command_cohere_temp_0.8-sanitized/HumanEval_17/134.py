from typing import List
pattern = 'o|_|.|'
def parse_music(music_string: str) -> List[int]:
    """Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return list of integers corresponding to how many beats does each
    note last.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    Args:
        music_string (str): musical string in the above format

    Returns:
        List[int]: beats per note of the parsed music string
    """
    converter = str.maketrans(pattern, '4 2 1')
    return [len(music_string[i:i+3]) // len(pattern) for i in range(0, len(music_string), 3)]