
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
    x = ""
    for i in string:
        if i == "[":
            x += i
        elif i == "]":
            x += i
            if x[-2:] == "]]" and x[-5:-3]!= "]]":
                x = x[:-2]
                return True
            elif x[-2:] == "[[" and x[-5:-3]!= "[":
                x = x[:-2]
                return True
            elif x[-1] == "]":
                x = x[:-1]
                return True
    return False

