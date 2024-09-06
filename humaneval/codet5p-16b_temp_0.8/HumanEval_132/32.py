
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

    
    if string.count('[') == string.count(']') and string.count('[') > 0:
        bracket_stack = []
        brackets = list(string)

        for i in range(len(brackets)):
            if brackets[i] == '[':
                bracket_stack.append('[')

            elif brackets[i] == ']':
                bracket_stack.pop()

            if brackets[i] == ']' and bracket_stack:
                continue

            else:
                return False

    else:
        return False

    return True
        
