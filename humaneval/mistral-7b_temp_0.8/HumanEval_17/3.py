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
    #parse = ''
    #last_beat = 0
    #while len(music_string) > 0:
    #    if 'o' in music_string:
    #        parse = 'o'
    #        last_beat = 4
    #    elif 'o|' in music_string:
    #        parse = 'o|'
    #        last_beat = 2
    #    elif '.' in music_string:
    #        parse = '.'
    #        last_beat = 1
    #    else:
    #        print('unrecognized character')
    #        break
    #    music_string = music_string.replace(parse, '')
    #    return last_beat

    #print(parse)
    return []

