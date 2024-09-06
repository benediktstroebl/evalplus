from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # 1. Can use stack to count the number of open paren and the max count of open paren at a particular index
    # 2. For each of the index, if the count of the max open paren is odd, then the deepest level of nesting is that level
    # 3. Can append this to a list
    stack = []
    max_open_paren = []
    for i in range(len(paren_string)):
        if paren_string[i] == '(':
            stack.append(i)
        elif paren_string[i] == ')':
            if len(stack) == 0:
                raise Exception('Parentheses are not balanced')
            stack.pop()
        if len(stack) > len(max_open_paren):
            max_open_paren.append(i)
        elif len(stack) == len(max_open_paren) and stack[-1] > max_open_paren[-1]:
            max_open_paren.append(stack[-1])

    # 4. If the length of stack is not zero then raise an error
    if len(stack) != 0:
        raise Exception('Parentheses are not balanced')
    # 5. For each of the index in the max_open_paren, if the count of the max open paren is odd, then the deepest level
    # of nesting is that level
    result = []
    for i in range(len(max_open_paren)):
        if i + 1 < len(max_open_paren) and max_open_paren[i + 1] - max_open_paren[i] > 1:
            result.append(i + 1)
        elif i + 1 == len(max_open_paren) and max_open_paren[i] - max_open_paren[i - 1] > 1:
            result.append(i + 1)
        else:
            result.append(max_open_paren[i])

    return result

