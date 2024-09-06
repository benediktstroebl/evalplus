
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

    brackets = {
        ']': '[',
        ')': '(',
        '}': '{'
    }
    stack = []
    for char in string:
        if char in brackets.values():
            stack.append(char)
        elif char in brackets.keys():
            if stack:
                if stack[-1] == brackets[char]:
                    stack.pop()
                else:
                    return False
            else:
                return False
    if stack:
        return False
    return True
