
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
    length = 0
    nesting = 0
    for char in string:
        if char == '[':
            stack.append(nesting)
            length += 1
            nesting += 1
        elif char == ']':
            if stack[-1] == nesting:
                nesting -= 1
                if length - nesting + 1 >= nesting:
                    nesting = length - nesting + 1
                    stack.pop()
            else:
                return False
        else:
            length += 1
    return True