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
    output = []
    for i in range(len(music_string) // 2):
        curr_string = ''
        curr_num = 0
        curr_state = ''
        for char in music_string[2 * i: 2 * (i + 1)]:
            if char == 'o' and curr_state == '':
                curr_state = 'o'
                curr_string = ''
                curr_num = 1
            elif char == 'o' and curr_state == 'o':
                curr_num += 1
                curr_state = 'o'
                curr_string = ''
            elif char == 'o' and curr_state == 'o|':
                curr_num += 1
                curr_state = 'o'
                curr_string = ''
            elif char == 'o' and curr_state == '.|':
                curr_num += 1
                curr_state = 'o'
                curr_string = ''
            elif char == 'o' and curr_state == 'o|.':
                curr_num += 1
                curr_state = 'o|'
                curr_string = ''
            elif char == 'o' and curr_state == 'o|..':
                curr_num += 1
                curr_state = 'o|'
                curr_string = ''
            elif char == 'o' and curr_state == 'o|...':
                curr_string += '..'
                curr_num += 1
                curr_state = 'o|'
                curr_string = ''
            elif char == 'o' and curr_state == 'o..':
                curr_num += 1
                curr_string += '..'
                curr_state = 'o'
                curr_string = ''
            elif char == 'o' and curr_state == 'o...':
                curr_num += 1
                curr_string += '...'
                curr_state = 'o'
                curr_string = ''
            elif char == 'o' and cur