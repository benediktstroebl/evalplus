
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
    # [ ] [ ] [ ] [ ] [ ] ➞ True
    # [ ] [ ] [ ] [ ] ➞ False
    # [ ] [ ] [ ] [ ] [ ] [ ] ➞ True
    # [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] ➞ False
    # [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] ➞ True
    # [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] ➞ False

    s = ""
    for i in string:
        if i == "]":
            if s == "[":
                s = ""
            else:
                s = s[:-1]
        else:
            s += i
    if s != "":
        return True
    return False
