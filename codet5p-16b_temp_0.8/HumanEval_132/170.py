
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

    
    open_bracket = []
    brackets = {']': '[', '}': '{', ')': '('}
    
    for i in string:
        if i in brackets.values():
            open_bracket.append(i)
        elif i in brackets:
            if not open_bracket:
                return False
            elif brackets[i]!= open_bracket.pop():
                return False

    return not open_bracket

