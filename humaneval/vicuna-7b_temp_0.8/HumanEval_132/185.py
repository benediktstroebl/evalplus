
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
    last_open = False
    
    for i, c in enumerate(string):
        if c == '[':
            if not last_open:
                stack.append(i)
                last_open = True
            else:
                stack[-1] = max(stack[-1], i)
        
        elif c == ']':
            if not last_open:
                return False
            stack.pop()
            last_open = False
        
        elif c == ']':
            last_open = False
        
    return stack[-1] == len(string) - 1

print(is_nested("[[]]")) # True
print(is_nested("[]]]]]]][[[[[]")) # False
print(is_nested("[][]")) # False
print(is_nested("[]")) # False
print(is_nested("[[][]]")) # True
print(is_nested("[[]][[")) # True