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
    notes = list(music_string)
    start_index = 0
    subseqs = []
    while start_index < len(notes):
        end_index = start_index + 1
        while end_index < len(notes):
            if notes[end_index] == 'o':
                end_index += 1
            else:
                break
        if end_index + 1 == start_index:
            subseqs.append(1)
            start_index += 1
        else:
            if notes[start_index] == 'o':
                subseqs.append(1)
                start_index += 1
            elif notes[end_index] == 'o':
                subseqs.append(2)
                start_index = end_index
            else:
                subseqs.append(1)
                start_index = end_index
    return subseqs

