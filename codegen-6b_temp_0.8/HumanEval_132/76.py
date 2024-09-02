
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
    for char in string:
        if char == '[' or char == '[' or char == ']':
            list.append(char)
        else:
            if not list:
                return False
            else:
                print(list[-1])
                if list[-1] == '[' and char == ']':
                    list.pop()
                elif list[-1] == '[' and char == ']':
                    list.pop()
                elif list[-1] == '[' and char == ']':
                    list.pop()
                else:
                    return False
    if list.__len__() == 0:
        return True
    else:
        return False

