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

    # List of durations for each note
    durations = [4, 2, 1]

    # Convert music string into list of strings
    music_list = music_string.split()

    # Convert each string into list of characters
    music_list = [list(note) for note in music_list]

    # Convert each character into integer corresponding to duration
    music_list = [[durations.index(int(char)) for char in note] for note in music_list]

    # Add up the duration of each note
    music_list = [sum(note) for note in music_list]

    return music_list
