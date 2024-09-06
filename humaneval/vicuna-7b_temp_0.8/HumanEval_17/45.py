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
    # Define the regular expression pattern that matches notes
    pattern = r'o( o| |\. |\.| )o( o| |\. |\.| )o( o| |\. |\.| )\*(?= o| |\. |\.| )'

    # Use re.findall() to extract all matches of the pattern from the string
    matches = re.findall(pattern, music_string)

    # Return the list of integers corresponding to the number of beats for each note
    return [int(note) for note in matches]

