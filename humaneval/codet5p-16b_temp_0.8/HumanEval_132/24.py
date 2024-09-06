
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

    
    brackets = []
    for c in string:
        if c == '[' or c == ']' or c == '{' or c == '}':
            brackets.append(c)
    
    if brackets == []:
        return False
    
    for i in range(len(brackets)):
        if brackets[i] == ']' and brackets[i-1] == '[':
            return True
        elif brackets[i] == '}' and brackets[i-1] == '{':
            return True
    
    return False

