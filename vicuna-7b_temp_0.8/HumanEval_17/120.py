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
    note_stack = []
    for char in music_string:
        if char in ['o', '|']:
            # push note to note_stack
            if note_stack:
                current_note = note_stack[-1]
                # add half note if it's last note in current_note
                if current_note == 'o':
                    beats.append(2)
                else:
                    beats.append(1)
            # pop note from note_stack
            note_stack.pop()
        elif char == '.':
            # push note to note_stack
            if note_stack:
                current_note = note_stack[-1]
                # add quarter note if it's last note in current_note
                if current_note == 'o':
                    beats.append(1)
                else:
                    beats.append(0)
            # pop note from note_stack
            note_stack.pop()
    return beats

