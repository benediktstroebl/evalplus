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
    for note in music_string.split("\n"):
        # split the note to see if it's whole, half, or quarter
        note_parts = note.split("|")
        if len(note_parts) > 1:
            # if the note has more than one part, it's a fraction
            start, end = note_parts[0], note_parts[1]
            # add the fraction to the beats list
            beats.append(int(start))
        else:
            # if the note has only one part, it's a whole or half note
            if "o" in note_parts[0]:
                # if it's a whole note, add the length of the note to the beats list
                beats.append(int(note_parts[0]))
            elif "." in note_parts[0]:
                # if it's a half note, add the length of the note to the beats list
                beats.append(int(note_parts[0]))
    return beats

