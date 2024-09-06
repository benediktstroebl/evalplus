
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

    # 1. SOLUTION:
    # return any(is_nested(x) for x in string.split(']')[1:])

    # 2. SOLUTION:
    # return any(is_nested(string[i:]) for i in range(len(string)))

    # 3. SOLUTION:
    # return any(is_nested(string[i:]) for i in range(len(string) - 1))

    # 4. SOLUTION:
    # return any(is_nested(string[i:]) for i in range(len(string))) or string.startswith('[')

    # 5. SOLUTION:
    return string.startswith('[') or any(is_nested(string[i:]) for i in range(len(string)))
