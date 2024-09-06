
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
    brackets = []
    if not string:
        return True
    elif string == '[]':
        return True
    else:
        for char in string:
            if char == '[':
                brackets.append(char)
            elif char == ']':
                if len(brackets) > 0 and brackets.pop() == '[':
                    continue
                else:
                    return False
        if len(brackets) == 0:
            return True
        else:
            return False

