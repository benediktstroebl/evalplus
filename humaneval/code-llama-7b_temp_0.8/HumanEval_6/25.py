from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # k - number of open brackets we see so far
    # level - the deepest level we've seen so far
    # index - index of character in string to process
    # result - list of results to return

    def helper(k: int, level: int, index: int, result: List[int]):
        if index == len(paren_string):
            # check if the result is empty, if so it means that the last open bracket wasn't closed
            if level == 0 and result == []:
                result.append(-1)
            else:
                result.append(level)
            return
        # check if next character is an open bracket
        if paren_string[index] == '(':
            k += 1
        # if it's a close bracket, and the number of open brackets we've seen is 0
        # then it means that we've reached the end of the current nested group
        # so we check if the current level of nesting is higher than the max level we've seen so far
        # if it is, we update the max level to the current level
        # then we reset the number of open brackets we've seen so far to 0
        elif paren_string[index] == ')':
            k -= 1
            if k == 0 and level > max_level:
                max_level = level
            k = 0
        # we recursively call the helper with an updated k value
        # and an increased level counter
        # we also pass the index of the next character in the string to process
        helper(k, level + 1, index + 1, result)

    result: List[int] = []
    max_level = 0
    helper(0, 0, 0, result)
    return result

