
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
    lst = list(string)
    if len(lst) == 1:
        return False
    elif lst[0] == '[':
        lst.pop(0)
    elif lst[-1] == ']':
        lst.pop()
    elif lst[0] == '[' and lst[-1] == ']':
        lst.pop(0)
        lst.pop()
        return True
    else:
        return False



    for i in range(len(lst)):
        if lst[i] == '[':
            if i == len(lst) - 1:
                return True
            else:
                if lst[i+1] == ']':
                    lst[i] = ' '
                    lst.pop(i+1)
                    return True
                else:
                    lst.pop(i)
                    return is_nested(lst)
        elif lst[i] == ']':
            if i == 0:
                return True
            else
