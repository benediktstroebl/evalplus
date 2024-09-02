
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
    if len(string) == 1:
        return False
    for i in string:
        if i == '[':
            brackets.append(i)
        else:
            if brackets == []:
                return False
            else:
                if brackets[-1] == '[':
                    brackets.pop()
                else:
                    return False
    return True
