
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
    l = []
    for i in string:
        if i == "[" or i == "]":
            l.append(i)
    l1 = len(l)
    count = 0
    for i in range(l1):
        if l[i] == "[":
            count += 1
        elif l[i] == "]":
            count -= 1
        if count < 0:
            return True
    return False
    # Code here
    pass

