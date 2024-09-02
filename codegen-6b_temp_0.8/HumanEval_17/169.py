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
    input_list = list(music_string)
    result_list = []

    def count_beats(input_string: str):
        """ Counts beats in one string of musical notes"""
        beats = 0
        for char in input_string:
            if char == 'o':
                beats += 1
            elif char == 'o|':
                beats += .5
            elif char == ':|':
                beats += .25
            else:
                raise ValueError('Unhandled char: {}'.format(char))
        return beats

    for item in input_list:
        if item == 'o':
            result_list.append(1)
        elif item == 'o|':
            result_list.append(.5)
        elif item == ':|':
            result_list.append(.25)
        else:
            raise ValueError('Unhandled char: {}'.format(item))

    return result_list

