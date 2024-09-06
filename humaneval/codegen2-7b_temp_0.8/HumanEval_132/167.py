
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
    result = False
    arr = []
    for i in string:
        if i == '[' and not arr:
            arr.append(i)
            continue
        if i == ']' and not arr:
            arr.append(i)
            continue
        if i == ']' and arr and arr[-1] == '[':
            arr.pop()
            continue
        if i == '[' and arr and arr[-1] == '[':
            arr.pop()
            continue
        if i == ']' and arr:
            arr.pop()
            continue
        if not arr:
            result = False
            break
    return
