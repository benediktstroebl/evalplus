
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
    left = []
    bracket = []
    for c in string:
        if c in ['[', '(', '{']:
            bracket.append(c)
            left.append(c)
        else:
            if len(bracket) == 0 or (c != ']' and c != ')' and c != '}'):
                return False
            elif c == ']' and '[' not in left:
                return False
            elif c == ')':
                if not left:
                    return False
                elif left[-1] == '(':
                    left.pop()
                else:
                    return False
            elif c == '}':
                if not left:
                    return False
                elif left[-1] == '{':
                    left.pop()
                else:
                    return False
    return True if not left and len(bracket) == 0 else False
