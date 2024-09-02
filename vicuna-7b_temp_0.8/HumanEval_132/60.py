
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
    i = 0
    while i < len(string):
        if string[i] == '[' and i < len(string) - 1 and string[i + 1] == '[':
            stack.append(i)
            i += 2
        elif string[i] == ']' and i < len(string) - 1 and string[i - 1] == '[':
            if stack:
                j = stack.pop()
                i = j + 1
                while i < len(string) and string[i] == '[':
                    i += 1
                if i >= len(string):
                    return True
                stack.append(i)
                i += 1
        elif string[i] == ']':
            if i > 0 and string[i - 1] == '[':
                return True
    return False