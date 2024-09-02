from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # Define a function to count the number of open and closed parentheses
    def count_open_close(s):
        count_open, count_close = 0, 0
        for char in s:
            if char == '(':
                count_open += 1
            elif char == ')':
                count_close += 1
        return count_open - count_close

    # Define a helper function to find the longest matching substrings
    def longest_match(s, t):
        # Create two dictionaries to store the longest matching substrings
        A = {}
        B = {}
        for char in s:
            A[char] = 1
        for char in t:
            B[char] = 1
        for char in s:
            for char2 in t:
                if char == char2:
                    A[char] += A[char2]
                    del B[char2]
                    break
        for char in t:
            for char2 in s:
                if char == char2:
                    B[char] += B[char2]
                    del A[char2]
                    break
        # Compare the two dictionaries and return the longer one
        if len(A) > len(B):
            return A
        else:
            return B

    # Define a helper function to find the maximum number of nested parentheses
    def max_nesting(s):
        return longest_match(s, '(') - longest_match(s, ')')

    # Parse the input string and return the result
    result = []
    for s in paren_string.split():
        count = max_nesting(s)
        result.append(count)
    return result
