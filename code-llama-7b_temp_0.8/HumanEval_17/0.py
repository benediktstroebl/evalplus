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
    # split the string into a list of words
    split_string = music_string.split()

    # initialize a variable to hold the length of each beat
    beat_length = 0

    # initialize a list to hold the number of beats for each note
    notes_list = []

    # loop through the words in the list
    for word in split_string:
        # reset beat_length if it is a whole note
        if word == 'o':
            beat_length = 4
        # set beat length to 2 if it is a half note
        elif word == 'o|':
            beat_length = 2
        # set beat length to 1 if it is a quater note
        elif word == '.|':
            beat_length = 1
        # if it is neither of these, add beat length to notes list
        else:
            notes_list.extend([beat_length] * int(word))

    return notes_list

