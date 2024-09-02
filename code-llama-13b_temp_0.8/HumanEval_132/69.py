
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
    arr = []
    for x in string:
        if x == '[':
            arr.append('start')
        if x == ']':
            arr.append('end')
    #print(arr)
    if arr.count('end') == arr.count('start'):
        return False
    else:
        return True


