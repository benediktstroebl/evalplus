from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    def count_parens(paren_string: str) -> int:
        """
        Helper function to count the number of opening parentheses in a string.
        """
        return len(find_parens(paren_string))

    def find_parens(paren_string: str) -> List[str]:
        """
        Helper function to find all occurrences of opening and closing parentheses in a string.
        """
        count = 0
        stack = [paren_string]
        result = []

        while stack:
            c = stack[-1]
            if c == '(':
                stack.append(c)
            elif c == ')':
                stack.pop()
            else:
                result.append(c)

        return result

    def process_group(open_parens: List[str]) -> List[int]:
        """
        Helper function to process a group of nested parentheses.
        """
        count = 0
        for c in open_parens:
            if c == '(':
                count += 1
            elif c == ')':
                count -= 1

        return count

    paren_string = paren_string.strip()
    open_parens = find_parens(paren_string)
    result = [process_group(open_parens)]

    while open_parens:
        open_parens = find_parens(open_parens[0])
        result.append(process_group(open_parens))

    return result
