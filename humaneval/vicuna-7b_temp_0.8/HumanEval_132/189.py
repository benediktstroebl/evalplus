
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
    for char in string:
        if char == '[':
            stack.append(char)
        elif char == ']':
            if stack:
                stack.pop()
                if stack[-1] == ']':
                    stack.pop()
        elif char == '(':
            # Start a nested subsequence
            nesting = 1
            while nesting:
                char = stack.pop()
                nesting -= 1
                if char == ']':
                    nesting -= 1
                elif char == '(':
                    nesting += 1
            stack.pop()
        else:
            stack.append(char)
    return stack == []
