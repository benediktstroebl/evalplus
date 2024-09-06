
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
    count = 0
    for char in string:
        if char == ']':
            count += 1
        elif char == '[':
            stack.append(char)
        elif char == ']':
            while stack and stack[-1] != '[':
                stack.pop()
            if count > 0:
                count -= 1
        elif char == '[':
            if stack and not stack[-1] == '[':
                count += 1
            stack.append(char)
    return count > 0
