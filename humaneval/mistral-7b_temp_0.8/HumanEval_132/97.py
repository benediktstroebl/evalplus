
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

    # 풀이 1
    cnt = 0
    for i in string:
        if i == '[':
            cnt += 1
        elif i == ']':
            cnt -= 1
    return cnt != 0

    # 풀이 2
    # return '[' in string or ']' in string and ']' in string and '[' in string

    # 풀이 3
    # return '[' in string and ']' in string and (string.count('[') != string.count(']'))

    # 풀이 4
    # return '[' in string and ']' in string and string.count('[') > string.count(']')
