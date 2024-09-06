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
    # Convert the music string to a list of characters
    music_list = list(music_string)

    # Initialize the list of beat lengths
    beat_lengths = []

    # Append the length of the first whole note to the list
    beat_lengths.append(4)

    # Iterate through the list of characters, starting from the second
    for beat_length in music_list[1:]:

        # If the character is 'o', append 4 to the list
        if beat_length == 'o':
            beat_lengths.append(4)

        # If the character is 'o|', append 2 to the list
        elif beat_length == 'o|':
            beat_lengths.append(2)

        # If the character is '.|', append 1 to the list
        elif beat_length == '.|':
            beat_lengths.append(1)

    return beat_lengths

