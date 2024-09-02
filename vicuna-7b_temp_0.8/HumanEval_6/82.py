from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    def parse_one_group(paren_string: str) -> int:
        nesting = 0
        for opening, closing in ((r'((', r'))'), (r'\(', r'\)')):
            for i in range(nesting + 1):
                match = re.search(opening + r'(\d+)(?)' + closing, paren_string)
                if match:
                    return nesting + int(match.group(1))
            nesting += 1
        return nesting

    def parse_nested(paren_string: str) -> List[int]:
        nesting = 0
        stack = []
        result = []
        for i, c in enumerate(paren_string):
            if c == '(':
                nesting += 1
                result.append(nesting)
            elif c == ')':
                nesting -= 1
                stack.pop()
                if len(stack) == 0:
                    break
            else:
                stack.append(i)
        return result

    return parse_nested(paren_string)