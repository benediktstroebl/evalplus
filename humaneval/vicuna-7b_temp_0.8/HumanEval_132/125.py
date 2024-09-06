
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
    # Example test cases
    test_cases = [
        ['[]', True],
        ['[]]', True],
        ['[]]]]', True],
        ['[][[[]', True],
        ['[][', False],
        ['[]', False],
        ['[]]', False],
        ['[][]', False],
        ['[][]', False],
        ['[][]', False],
        ['[][]', False],
    ]

    for test_case in test_cases:
        if is_valid_subsequence(test_case[0], test_case[1]):
            return True
    return False
