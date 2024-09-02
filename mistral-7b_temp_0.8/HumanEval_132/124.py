
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

    # Brackets must be '[]'
    # Then, we have to use a stack to check if a string contains nested brackets.
    # For this, we have to follow the following rules:
    # 1. If the current character is an '[' then, we have to push it to the stack.
    # 2. If the current character is a ']', then, we have to check if the last character in the stack is a '['.
    #    If yes, then, pop it from the stack. If the stack is empty, then, return False.
    # 3. If the last character in the stack is not a '[' and the current character is a ']', then, return False.
    # 4. If the stack is not empty, then, return True.

    brackets = '[]'
    stack = []
    for i in string:
        if i == brackets[0]:
            stack.append(i)
        elif i == brackets[1]:
            if not stack:
                return False
            elif stack and stack[-1] == brack
