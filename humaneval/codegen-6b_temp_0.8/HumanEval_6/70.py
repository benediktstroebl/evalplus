from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    list_of_parens = paren_string.split()
    list_of_parens = [[x] if x != '(' else [] for x in list_of_parens]
    counter = 0
    for i in range(len(list_of_parens)):
        if list_of_parens[i] == []:
            continue
        parens_in_list = 0
        while counter < len(list_of_parens) - i:
            if list_of_parens[counter + i] != []:
                counter += 1
                parens_in_list += 1
                list_of_parens[counter + i] += list_of_parens[counter]
                list_of_parens[counter] = []
            else:
                counter += 1
        if parens_in_list < i + 1:
            list_of_parens[i] = 0
        else:
            list_of_parens[i] = parens_in_list
    return [x for x in list_of_parens if x != []]

