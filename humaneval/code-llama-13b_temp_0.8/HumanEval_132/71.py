
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
    l, r = 0, 0
    string = list(string)
    for el in string:
        if el == '[':
            l += 1
        elif el == ']':
            if l == 0:
                r += 1
            else:
                l -= 1
    return (r > 0) or (l != 0)

