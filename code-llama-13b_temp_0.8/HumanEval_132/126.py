
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
    def is_valid(string):
        a = []
        for s in string:
            if s == '[':
                a.append(s)
            else:
                if len(a) == 0:
                    return False
                else:
                    a.pop()
        return len(a) == 0
    nested = False
    for i in range(1, len(string)):
        if is_valid(string[:i]) and is_valid(string[i:]):
            nested = True
    return nested


