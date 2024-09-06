
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
    if (len(string) == 2) or (len(string) == 0):
        return False
    if string[0] == '[' and string[-1] == ']':
        return is_nested(string[1:-1])
    else:
        b = 0
        s = []
        for i in string:
            if i == '[':
                b += 1
                s.append(i)
            elif i == ']':
                b -= 1
                s.append(i)
        return b != 0 or is_nested(''.join(s))

