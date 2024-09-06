
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
    for bracket in string:
        if len(brackets) == 0:
            brackets.append(bracket)
        else:
            if brackets[-1] == '[' and bracket == ']':
                brackets.pop()
            else:
                brackets.append(bracket)
    return len(brackets) == 0
