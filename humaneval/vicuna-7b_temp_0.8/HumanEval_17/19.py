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
        if char == ':':
            # move to next line
            continue
        elif char == 'o':
            # whole note
            for i in range(len(note_stack) - 3):
                beats.append(4)
        elif char == 'o|':
            # half note
            for i in range(len(note_stack) - 1):
                beats.append(2)
        elif char == '.':
            # quarter note
            for i in range(len(note_stack) - 3):
                beats.append(1)
        elif char == '|':
            # add the current note to the stack
            note_stack.append(len(note_stack) - 1)
        else:
            # pop the current note from the stack and add the next one
            note_stack.pop()
            note_stack.append(0)
    return beats
