
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
    nest = 0
    for i in range(len(string)):
        if string[i] == '[':
            stack.append(i)
        elif string[i] == ']':
            if len(stack) == 0:
                return False
            else:
                start = stack.pop()
                if i - start == 1:
                    nest += 1
                else:
                    if nest > 0:
                        return True
    if nest > 0:
        return True
    else:
        return False

