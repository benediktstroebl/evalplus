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
    lst = music_string.split(' ')
    lst = [x for x in lst if x != '']
    lst = list(filter(lambda x: x != 'o', lst))
    lst = list(filter(lambda x: x != '.', lst))
    lst = list(filter(lambda x: x != '|', lst))
    lst = list(filter(lambda x: x != 'o|', lst))

    # print(lst)
    print(len(lst))

    # parser = re.compile('o o\.*\|o\.*\|\.|\.|\.|\.|')
    # parser = re.compile('o o\.*\|o\.*\|\.|\.|\.|\.|\.|')
    # parser = re.compile('o o\.*\|o\.*\|\.|\.|\.|\.|\.|\.|\.|')
    # result = parser.split(music_string)
    # print(result)

    return sum([len(x) for x in lst])

