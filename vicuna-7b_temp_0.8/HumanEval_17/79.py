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
    current_note = None
    for char in music_string:
        # check if this is a note start
        if char == 'o':
            # if this is a whole note, increment the beat count
            if current_note is None:
                beats.append(current_beat)
                current_beat += 4
            elif current_note == 'o':
                beats.append(current_beat)
                current_beat += 2
            else:
                beats.append(current_beat)
                current_beat += 4
                current_note = 'o'
        # check if this is a note end
        elif char == '|':
            # if this is a note, append it and reset the note and beat counters
            if current_note is None:
                beats[-1] += 2
                current_beat -= 2
            else:
                beats.append(current_beat)
                current_beat += 2
                current_note = None
        # check if this is a dot and the previous note was a whole note
        elif char == '.' and current_note == 'o':
            # increment the beat count
            beats.append(current_beat)
            current_beat += 1
        else:
            current_note = char
    # if this is a whole note and the next character is a dot, append the rest of the beat count
    if current_note == 'o' and char == '.':
        beats[-1] += 1
    # return the list of beats
    return beats