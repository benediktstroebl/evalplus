from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # parse all possible pairs of opening and closing parentheses
    pair_tuples = [(index, -1) for index, _ in enumerate(paren_string)]
    # print(pair_tuples)

    for index, char in enumerate(paren_string):
        if char == "(":
            pair_tuples[index] = (index, 0)
        elif char == ")":
            if pair_tuples[index][1] == -1:
                pair_tuples[index] = (index, 1)
                pair_tuples[pair_tuples[index][0]][1] += 1

    # print(pair_tuples)
    ans = []

    for index, level in pair_tuples:
        if level == -1:
            ans.append(index)

    return [len(ans)] + ans[::-1]

