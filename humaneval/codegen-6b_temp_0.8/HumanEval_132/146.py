
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
    l = len(string)
    br_stack = []
    for i in range(l):
        if string[i] == '[' and len(br_stack) == 0:
            br_stack.append(i)
        elif string[i] == '[' and len(br_stack) > 0:
            br_stack.append(i)
        elif string[i] == ']' and len(br_stack) > 0:
            br_stack.pop()
        elif string[i] == ']' and len(br_stack) == 0:
            br_stack.append(i)
        elif string[i] == ')':
            print(i, br_stack)
            if len(br_stack) == 0:
                return True
    return False
