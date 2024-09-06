
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
    # return any(char in string for char in ['[[']) and any(char in string for char in [']'])

    left = []
    right = []

    for i,char in enumerate(string):
        if char == '[':
            left.append(i)
        elif char == ']':
            # print(left[-1])
            right.append(i)

    if right and left[-1] == right[-1]:
        return True
    else:
        return False

