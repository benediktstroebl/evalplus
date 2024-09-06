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
    notes_list = music_string.split('|')
    notes = [0] * len(notes_list)
    index = 0
    for note in notes_list:
        count = 0
        while note[count] == '.':
            count += 1
        if note[count] == 'o':
            for i in range(count):
                notes[index] += 1
            index += 1
        else:
            notes[index] += int(note[count])
    return notes

