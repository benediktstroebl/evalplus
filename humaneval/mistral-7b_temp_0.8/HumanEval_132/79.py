
def is_nested(string):
    '''
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if there is a valid subsequence of brackets 
    where at least one bracket in the subsequence is nested.

    is_nested('[[]]') ➞ True
    is_nested('[]]]]]]][[[[[]') ➞ False
    is_nested('[][]') ➞ False
    is_nested('[]') ➞ False
    is_nested('[[][]]') ➞ True
    is_nested('[[]][[') ➞ True
    '''

    # 3 ^ n
    # 1. Find the longest subsequence of brackets
    # 2. Check if the longest subsequence contains any nested brackets

    def is_nested_helper(string, i, longest_subsequence, n_nested_brackets):
        if len(string) - i < n_nested_brackets:
            # Too few characters remaining
            return False

        if len(string[i:]) - n_nested_brackets < longest_subsequence:
            # Too few characters remaining to form a longer subsequence
            return False

        if string[i] == '[':
            return is_nested_helper(string, i + 1, longest_subsequence, n_nested_brackets + 1)
        elif string[i] == ']':
            if n_nested_brackets > 0:
                return is_nested_helper(string, i + 1, longest_subsequence, n_nested_brackets - 1)
            else:
                return is_nested_helper(string,
