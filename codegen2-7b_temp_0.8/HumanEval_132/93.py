
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
    if not isinstance(string, str):
        return False
    s = []
    for i in string:
        if i == '[' or i == '{' or i == '(' :
            s.append(i)
            continue
        else:
            if not s:
                return False
            else:
                if s[-1] == '[' or s[-1] == '{' or s[-1] == '(' :
                    s.pop()
                    continue
                else:
                    return False
    return True
