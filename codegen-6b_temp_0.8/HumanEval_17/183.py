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
    result = []
    index = 0

    last_note = 'o'
    last_note_index = 0

    while index < len(music_string):
        note = music_string[index]
        if note == '(':
            index += 1
            notes_count = 0

            while index < len(music_string):
                note = music_string[index]
                if note == ')':
                    break
                if note in ['(', 'o', 'o|', 'o)']:
                    notes_count += 1
                index += 1
            index -= 1
            result.append(notes_count)
        else:
            index += 1

    return result

