
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
    opening_brackets = '[]'
    string = string.split(']')
    string.reverse()

    for brackets in string:
        if len(brackets) == 1:
            continue
        else:
            try:
                if brackets[0] == '[' and brackets[-1] == ']':
                    opening_brackets = ''.join(opening_brackets + brackets[1:-1])
            except:
                return False

    if opening_brackets == '':
        return True
    else:
        return False
