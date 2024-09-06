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
    notes = list(map(lambda c: c if c == "|" else None, music_string))
    beats = []

    for index, note in enumerate(notes):
        if note == "|":
            if notes[index - 1] == "o":
                beats.append(2)
            else:
                beats.append(1)
        elif note == "o":
            beats.append(4)
        elif note is None:
            pass
        else:
            raise ValueError(f"Unrecognized note: {note}")

    return beats

