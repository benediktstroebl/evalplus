
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
    mystack = []
    brackets = {')':'(',']':'[','}':'{'}
    for i, char in enumerate(string):
        if char in {'(','[','{'}:
            mystack.append(char)
        elif char == ')' and mystack.pop() != '(':
            return False
        elif char == ']' and mystack.pop() != '[':
            return False
        elif char == '}' and mystack.pop() != '{':
            return False
        else:
            continue
    return len(mystack) == 0
        
