
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
    start_index = 0
    for i in range(len(string)):
        if string[i] == '[' and stack:
            if stack[-1] != '[':
                return True
            stack.pop()
        elif string[i] == ']' and not stack:
            if stack[-1] != '[':
                return True
            stack.pop()
        elif string[i] == '[' and not stack:
            stack.append(string[i])
        elif string[i] == ']':
            if not stack:
                return False
            if stack[-1] != '[':
                return True
            stack.pop()
        else:
            if stack:
                start_index = stack[-1]
                stack.pop()
    return False

print(is_nested('[[]]')) # True
print(is_nested('[]]]]]]][[[[[]')) # False
print(is_nested('[][]')) # False
print(is_nested('[]')) # False
print(is_nested('[[][]]')) # True
print(is_nested('[[]][[')) # True