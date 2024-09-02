
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

    for i, bracket in enumerate(string):
        if bracket == '[' and i and string[i-1]!= ']':
            stack = []
            for j, bracket_ in enumerate(string[i+1:]):
                if bracket_ == ']':
                    stack.append(j)
                elif bracket_ == '[' and stack:
                    return True
                elif bracket_ == '[' and not stack:
                    break
    return False







