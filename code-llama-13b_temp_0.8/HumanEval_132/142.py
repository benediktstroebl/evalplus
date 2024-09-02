
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
    # SOLUTION:
    stack = []
    for i in string:
        if i == ']' and len(stack) > 0:
            if stack[-1] == '[':
                stack.pop()
            else:
                stack.append(i)
        elif i == '[':
            stack.append(i)
    return len(stack) == 0
    # return True if stack.pop() == '[' and len(stack) == 0 else False
    
    # A couple other solutions:
    # return '[]' in str(list(balanced_parentheses.solution(string)))
    # return stack.pop() == '[' and not stack
    
    
    
    # LAMBDAS:
    # return lambda x: len(x) == 0
    # return lambda x: not x
    
    # return lambda x: False if x == '[' else True
    
    # return lambda x: '[' in x
    
    
    
    # INPUTS:
    # is_nested('[[]]') ➞ True
    # is_nested('[]]]]]]][[[[[]') ➞ False
    # is_nested('[][]') ➞ False
    # is_nested('[]') ➞ False
    # is_nested('[[][]]') ➞ True
    # is_nested('[[]][[') ➞ True
