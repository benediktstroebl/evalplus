
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
    open_bracket_index = []
    for i in range(len(string)):
        if string[i] == '[':
            open_bracket_index.append(i)
        elif string[i] == ']':
            if open_bracket_index and open_bracket_index[-1] < i:
                return True
            elif open_bracket_index and open_bracket_index[-1] > i:
                open_bracket_index.pop()
            else:
                open_bracket_index.append(i)
    return False

