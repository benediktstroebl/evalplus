
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

    # Creating a Stack
    stack = []

    for i in string:
        # If the character is an opening bracket, we push it onto our stack.
        if i == '[':
            stack.append(i)
        # If the character is a closing bracket, we check to see if the stack is empty.
        # If the stack is empty, we know it is an invalid closing bracket.
        elif i == ']':
            if not stack:
                return False
            # If the stack is not empty, we pop off the top element.
            stack.pop()
    # If the stack is empty, we know that all brackets are properly nested.
    if stack == []:
        return True
    # If the stack is not empty, we know that there are still unmatched opening brackets.
    else:
        return False
