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
    all_notes = list(music_string)
    total = 0
    for i in range(len(all_notes)):
        note = all_notes.pop(0)
        if note == 'o':
            total += 1
        elif note == 'o|':
            total += 1 / 2
        elif note == '|':
            total += 1 / 4
        elif note == '.':
            continue
        else:
            all_notes.append(note)

    return [(total * 4 - 1)] * len(all_notes) + [total * 4] * (len(all_notes) - len(all_notes))

