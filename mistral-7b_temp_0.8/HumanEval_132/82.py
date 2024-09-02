
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
    index = 0
    count = 0
    list_1 = []
    while index < len(string):
        if string[index] == '[':
            count += 1
        if string[index] == ']':
            count -= 1
            if count < 0:
                return False
        list_1.append(count)
        index += 1
    if len(list_1) > 0:
        for count in list_1:
            if count < 0:
                return True
    return False
