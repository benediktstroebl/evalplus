from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # result = parens.split(' ')
    # for i in range(len(parens)):
    #     parens[i] = parens[i].replace('(', '').replace(')', '')
    #     parens[i] = parens[i].split(' ')
    # result = filter(lambda x: len(x) > 0, parens)
    # result.reverse()
    # print(result)
    # return [len(x) for x in result]
    # print(list(map(lambda x: len(x), result)))
    max_level = 0
    for paren in paren_string.split(' '):
        level = 0
        for char in paren:
            level += 1 if char == '(' else -1
        max_level = max(max_level, level)
    return [max_level]

