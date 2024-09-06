
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
    for symbol in string:
        if symbol == '[':
            stack.append(symbol)
        elif symbol == ']':
            while stack:
                if stack[-1] != '[':
                    return False
                stack.pop()
        elif symbol == '(':
            while symbol != '[':
                stack.append(symbol)
                symbol = input()
            stack.pop()
            stack.pop()
            if stack and stack[-1] == ')':
                return False
        elif symbol == ']':
            if stack and stack[-1] != '[':
                return False
    return True
