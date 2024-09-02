
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

    
    if string.count('[]') == 1:
        return True
    elif string.count('[]') == 0:
        return False
    else:
        brackets = list(string)
        brackets_2 = []
        for char in brackets:
            if char == '[':
                brackets_2.append(char)
            else:
                if len(brackets_2) > 0:
                    brackets_2.pop()
        if brackets_2 == []:
            return True
        else:
            return False
                
