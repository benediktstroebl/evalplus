from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    nesting_counts = [0] * 5
    stack = [0]
    result = [0]
    start = 0
    for i in range(len(paren_string)):
        while i < len(paren_string) and paren_string[i] == '(':
            i += 1
            while paren_string[i] == '(':
                i += 1
            nesting_counts[stack[-1]] += 1
            if i >= len(paren_string):
                break
        if i == len(paren_string):
            break
        while paren_string[i] == ')':
            i += 1
            nesting_counts[stack[-1]] -= 1
            if i == len(paren_string):
                break
            stack.append(i)
        result[0] = nesting_counts[stack[-1]]
        start = i + 1
        for j in range(1, len(nesting_counts)):
            result[j] = max(result[j], nesting_counts[stack[-1]] - nesting_counts[j])
    return result

