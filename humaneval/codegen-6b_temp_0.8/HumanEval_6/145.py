from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    def parse(stack, i, last_level):
        if i < len(paren_string):
            if paren_string[i] == ')':
                if stack:
                    stack.pop()
                else:
                    return False
            elif paren_string[i] == '(':
                stack.append(0)
            elif paren_string[i].isdigit():
                j = i
                while j < len(paren_string) and paren_string[j].isdigit():
                    j += 1
                if last_level < stack[-1] + int(paren_string[i:j]):
                    last_level = stack[-1] + int(paren_string[i:j])
                stack[-1] = last_level
                i = j
            else:
                return False
            i += 1
            return parse(stack, i, last_level)
        return True

    return list(map(lambda x: x + 1, parse([], 1, 0)))

