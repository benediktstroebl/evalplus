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
    # Split the string in to a list of all notes.
    split_str = music_string.split(' ')
    # Initialize an empty list to store the beats of each note.
    list_of_beats = []
    # Loop through each note in the split_str.
    for note in split_str:
        # Initialize a counter for the beats of each note.
        counter = 0
        # Loop through each character in the note.
        for character in note:
            # If the character is 'o', or 'o|', add a whole note to the counter.
            if character == 'o':
                counter += 1
            # If the character is 'o|', add a half note to the counter.
            elif character == 'o|':
                counter += .5
            # If the character is '.|', add a quarter note to the counter.
            elif character == '.':
                counter += .25
        # After the loop is finished, append the counter to the list_of_beats.
        list_of_beats.append(counter)
    # After the loop is finished, return the list_of_beats.
    return list_of_beats

