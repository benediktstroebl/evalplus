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
    # get rid of all spaces, tabs, etc.
    music_string = music_string.replace(' ', '')
    # create a list of chars representing notes
    chars = list(music_string)
    # use a dict to store the numbers of beats, where keys are corresponding notes, and values are numbers
    # of beats
    counts = {}
    # iterate through all chars
    for char in chars:
        # if char is in counts, increment its value by 1
        if char in counts:
            counts[char] += 1
        # if char is not in counts, add it to the dict with value=1
        else:
            counts[char] = 1
    # create a list of beats
    beats = list(counts.values())
    # return the list of beats
    return beats

