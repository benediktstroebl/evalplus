
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
    # Checking if there are at least one '[' or ']' in the string
    if '[' not in string or ']' not in string:
        return False
    # Counting the numbers of brackets in the string
    cnt = 0
    for i in string:
        if i == '[':
            cnt += 1
        elif i == ']':
            cnt -= 1
        if cnt < 0:
            break
    return cnt == 0
