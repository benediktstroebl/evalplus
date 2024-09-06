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
    music = list(music_string)
    notes = ['o', 'o|', '.', '|']
    space = [' ']

    nums = []

    i = 0

    while i < len(music):
        if music[i] not in notes + space:
            i += 1
            continue

        if music[i] == ' ':
            i += 1
            continue

        if music[i] == 'o':
            nums.append(1)
            i += 1
            continue

        # Process 'o|'
        if music[i] == 'o|':
            while music[i] == 'o|':
                nums.append(0.5)
                i += 1
                if i == len(music) or music[i] == ' ':
                    break
            continue

        # Process 'o o'
        if music[i] == 'o o':
            while music[i] == 'o o':
                nums.append(0.25)
                i += 1
                if i == len(music) or music[i] == ' ':
                    break
            continue

        if music[i] == 'o':
            nums.append(0.25)
            i += 1
            continue

        if music[i] == '.':
            nums.append(1)
            i += 1
            continue

        if music[i] == '|':
            nums.append(0.5)
            i += 1
            continue

    return nums

