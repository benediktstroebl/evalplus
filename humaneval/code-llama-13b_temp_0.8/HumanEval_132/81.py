
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
    new_string = []
    stack = []
    
    for x in string:
        if x == '[':
            stack.append(x)
        else:
            if not stack:
                new_string.append(' ')
                new_string.append(x)
            else:
                stack.pop()
                new_string.append(x)

    if not stack:
        print(new_string)
        for x in range(len(new_string)-1):
            if new_string[x] == ' ':
                if new_string[x-1] != new_string[x+1]:
                    return True
    else:
        return False
    

