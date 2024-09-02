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

    notes_to_time = {'o': 4, 'o|': 2, '|': 1}
    parsed_music = []
    current_note = ''
    for c in music_string:
        if c in notes_to_time:
            current_note += c
        else:
            if current_note != '':
                parsed_music.append(notes_to_time[current_note])
            current_note = ''

    if current_note != '':
        parsed_music.append(notes_to_time[current_note])

    return parsed_music
