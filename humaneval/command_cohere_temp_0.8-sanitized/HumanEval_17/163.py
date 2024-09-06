from typing import List
pattern = '^ {0,2}(?:o|O|[.||]) ({1,3})?$'
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
    def note_duration(char: str) -> int:
        if char == 'o' or char == 'O':
            return 4
        if char == '|' or char == ' ':
            return 2
        return 1
    
    # regex pattern to check if string is a valid music string
    if not re.match(pattern, music_string):
        raise ValueError("Invalid music string")
    
    return [note_duration(char) for char in music_string]