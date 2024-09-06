
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
    # return ''.join([(i for i in string if i in '[]')]) == string
    res = ''
    for i in string:
        if i in '[]':
            if i == '[':
                res += i
            elif res[-1] == '[':
                res = res[:-1]
            elif res[-1] == ']':
                res += i
    return len(res) > 0

