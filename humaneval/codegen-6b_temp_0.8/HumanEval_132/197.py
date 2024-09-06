
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
    list = []
    for i in string:
        list.append(i)
    for i in range(len(list)):
        if list[i] == '[':
            list.append('[')
            list.remove('?')
            print(list)
        if list[i] == ']':
            list.remove('?')
            list.remove('[')
            print(list)
        if list[i] == '?':
            list.remove('?')
            list.remove('[' or ']')
            print(list)

    if len(list) == 0:
        return True
    else:
        return False
    
    