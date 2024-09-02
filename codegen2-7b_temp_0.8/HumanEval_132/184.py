
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
    lst = []
    for char in string:
        if char == '[' or char == '{' or char == '(' or char == '<':
            lst.append(char)
        else:
            if len(lst) == 0:
                return False
            else:
                if lst[-1] == '[':
                    lst.pop()
                elif lst[-1] == '{':
                    lst.pop()
                elif lst[-1] == '(':
                    lst.pop()
                elif lst[-1] == '<':
                    lst.pop()
                else:
                    return False
    return True
