from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    result = []

    for paren_group in paren_string.split():
        # The initial value of counter is 0.
        # Initially, there is no nesting.
        # As we encounter opening parenthesis, we increment it.
        # As we encounter closing parenthesis, we decrement it.
        counter = 0

        for char in paren_group:
            if char == '(':
                # If the value of counter is greater than zero,
                # then we know we have encountered nested parentheses.
                # As long as the value is greater than zero,
                # we keep incrementing the counter.
                counter += 1
            elif char == ')':
                # If the value of counter is greater than zero,
                # then we know we have encountered nested parentheses.
                # As long as the value is greater than zero,
                # we keep decrementing the counter.
                counter -= 1

        result.append(counter)

    return result

