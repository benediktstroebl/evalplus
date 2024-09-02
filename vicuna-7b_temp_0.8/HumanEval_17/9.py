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
    beats = []
    current_beat = 0

    for char in music_string:
        if char == 'd':
            # If there is a whole note following, add the current beat to the beats list
            if music_string[0] == 'o':
                beats.append(current_beat)
            current_beat += 4
        elif char == 'D':
            # If there is a whole note following, add the current beat to the beats list
            if music_string[0] == 'o':
                beats.append(current_beat)
            current_beat += 8
        elif char == 'h':
            # If there is a half note following, add the current beat and next beat to the beats list
            if music_string[0] == 'o':
                beats.append(current_beat)
                current_beat += 2
            else:
                beats.append(current_beat)
                current_beat += 1
        elif char == 'H':
            # If there is a half note following, add the current beat and next beat to the beats list
            if music_string[0] == 'o':
                beats.append(current_beat)
                current_beat += 2
            else:
                beats.append(current_beat)
                current_beat += 1
        elif char == 'p':
            # If there is a quarter note following, add the current beat to the beats list
            beats.append(current_beat)
        else:
            # If there is no whole, half or quarter note following, add the current beat to the beats list
            beats.append(current_beat)

    # Return the list of beats
    return beats

