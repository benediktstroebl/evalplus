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
    beats = [0] * 12  # 12 beats in a bar
    current_beat = 0  # current beat number

    for note in music_string:
        if note == 'o':
            beat = current_beat
            while 'o' in music_string[beat:beat + 2] or '|' in music_string[beat:beat + 2]:
                beat += 1
                if music_string[beat] == 'o':
                    beat += 1
                if music_string[beat] == '|':
                    beat += 2
            beats[current_beat] = beat - current_beat
            current_beat += 1
        elif note == '.':
            beats[current_beat] += 1
            current_beat += 1

    return beats