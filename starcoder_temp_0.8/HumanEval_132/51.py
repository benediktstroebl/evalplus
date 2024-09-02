
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
    brackets = ['[','{','(']
    open_brackets = []
    for char in string:
        if char in brackets:
            open_brackets.append(char)
        elif open_brackets:
            if char == ']':
                if open_brackets[-1] == '[':
                    open_brackets.pop()
                else:
                    return False
            elif char == '}':
                if open_brackets[-1] == '{':
                    open_brackets.pop()
                else:
                    return False
            elif char == ')':
                if open_brackets[-1] == '(':
                    open_brackets.pop()
                else:
                    return False
        else:
            return False
    return False if open_brackets else True



