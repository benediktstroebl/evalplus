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
    parse_list = []
    note_list = music_string.split(" o ")
    for i in note_list:
        if i == "o":
            parse_list.append(4)
        elif i == "o|":
            parse_list.append(2)
        elif i == '.|':
            parse_list.append(1)

    for i in range(len(parse_list)):
        count = 0
        if parse_list[i] == 4:
            for j in range(i, len(parse_list)):
                if parse_list[j] == 4:
                    count += 1
                else:
                    break
        elif parse_list[i] == 2:
            for j in range(i, len(parse_list)):
                if parse_list[j] == 4:
                    count += 1
                else:
                    break
        elif parse_list[i] == 1:
            for j in range(i, len(parse_list)):
                if parse_list[j] == 4:
                    count += 1
                else:
                    break
        else:
            continue

        parse_list[i] = count

    return parse_list

