from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    depth = 0
    max_depth = 0
    left_paren = '('
    right_paren = ')'
    paren_dict = {right_paren: -1, left_paren: 1}

    def update_depth(string: str, depth_mod: int):
        """
        :param string: string of parens or parenthesis
        :param depth_mod: the depth of the parens or parenthesis in the string
        :return:
        """
        for i in range(len(string)):
            if string[i] in paren_dict:
                paren_dict[string[i]] += depth_mod

    for i in range(len(paren_string)):
        if paren_string[i] == left_paren:
            depth += 1
            update_depth(paren_string, depth)
            max_depth = max(max_depth, depth)
        elif paren_string[i] == right_paren:
            depth -= 1
            update_depth(paren_string, depth)

    return [max_depth, max_depth - depth]

