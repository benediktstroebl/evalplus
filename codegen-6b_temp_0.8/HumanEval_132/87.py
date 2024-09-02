
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
    brackets = ['[', ']']
    bracket_stack = []
    for i in range(len(string)):
        if string[i] in brackets:
            if bracket_stack == []:
                return False
            else:
                if len(bracket_stack) > 0:
                    if string[i] == bracket_stack[0]:
                        if bracket_stack[-1] == '[':
                            bracket_stack.pop()
                        elif bracket_stack[-1] == ']':
                            bracket_stack.pop()
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
    return True
