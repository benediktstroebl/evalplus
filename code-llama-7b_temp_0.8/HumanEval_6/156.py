from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    depth_list = []
    for paren_group in paren_string.split():
        # The max depth is 2 * n - 2
        # This is because at each iteration, there are two things that can happen:
        # 1) We see an opening paren, then we increase our depth by 1.
        # 2) We see a closing paren, then we decrease our depth by 1.
        # Thus, after the nth iteration, we will have 2 * n - 2.
        # (()(())) -> 1 + 2 + 1 - 2 = 2
        # ((())) -> 1 + 2 + 2 - 2 = 3
        depth = 2 * len(paren_group) - 2

        # We need to make sure that the parentheses are balanced.
        # To do that, we need to count up how many open parens we see, and how many closing parens we see.
        # If the counts are equal, then we know that we don't have any extra parens, and we can simply take the
        # max of the two.
        # If the counts aren't equal, then we need to see how many extra parens we have.
        # To do that, we can subtract the max of the counts, which we know is non-negative, from the total number of
        # parens we saw. Then, the total number of extra parens will be max_count - max_count * 2 = max_count - 2.
        # Example: (())))
        # We see three opening parens, and two closing parens.
        # We have 5 parens in total.
        # Max count = 3.
        # Total paren count = 5 - 3 = 2.
        # Extra paren count = 3 - 3 * 2 = 1.
        # Thus, the number of extra parens is 1.
        open_paren_count = 0
        close_paren_count = 0
        for paren in paren_group:
            if paren == "(":
                open_paren_count += 1
            elif paren == ")":
                close
