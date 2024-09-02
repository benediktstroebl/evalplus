
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
    nest = False
    for char in string:
        if char == '[':
            stack.append(nest)
            nest = True
        elif char == ']':
            if not nest:
                return False
            nest = False
            while stack[-1] != []:
                pop = stack.pop()
                if pop == '[':
                    stack.append(nest)
                    nest = True
                elif pop == ']':
                    stack.pop()
                else:
                    return False
        elif char == '\\':
            if stack[-1] == '\\':
                stack.pop()
                stack.append(nest)
                nest = True
            elif stack[-1] == ']':
                return False
    return True