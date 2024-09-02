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

    music_beats = []
    current_beat = 0
    previous_note = 'o'

    for char in music_string.strip():
        if char == 'o':
            current_beat += 4
            music_beats.append(current_beat)
        elif char == '|':
            current_beat += 2
            music_beats.append(current_beat)
        elif char == '.':
            current_beat += 1
            music_beats.append(current_beat)
        elif char == 'o' and previous_note == '|':
            current_beat += 1
            music_beats.append(current_beat)
        else:
            music_beats = []
            break

        previous_note = char

    return music_beats

