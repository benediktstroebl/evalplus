
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

    stack = []
    brackets = {'[':']','{':'}','(':')'}
    for i in string:
        if i in brackets.keys():
            stack.append(i)
        else:
            if stack == []:
                return False
            if brackets[stack[-1]] == i:
                stack.pop()
    return stack == []

