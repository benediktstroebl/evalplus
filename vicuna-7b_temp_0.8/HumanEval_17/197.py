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
    for line in music_string.split('\n'):
        line = line.strip()
        if line == '':
            continue
        if line[0] == ':':
            note, rest = line.split('|')
            if note.endswith('o'):
                beats.append(4)
            elif note.endswith('.') and note[:2] != '00':
                beats.append(1)
            else:
                beats.append(0)
        else:
            rest_beats = 0
            for char in line:
                if char == 'o':
                    rest_beats += 2
                elif char == '|':
                    if rest_beats > 0:
                        beats.append(rest_beats)
                        rest_beats = 0
                elif char == '.':
                    if rest_beats == 0:
                        beats.append(rest_beats)
                        rest_beats = 1
                elif char == ' ':
                    rest_beats += 1
            if rest_beats > 0:
                beats.append(rest_beats)
    return beats

