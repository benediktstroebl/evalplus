
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
    nested_brackets = 0
    result = False
    if string[0] == '[' and not nested_brackets:
        bracket_stack = [0]
        bracket_stack.append(0)
        for i, c in enumerate(string):
            if i < len(string)-1:
                if c == '[' and string[i+1] == ']':
                    bracket_stack.append(i)
                elif c == ']' and string[i-1] != ']':
                    if i != bracket_stack[-1]:
                        bracket_stack.pop()
                        nested_brackets += 1
            else:
                if c == '[' and string[i-1] != ']':
                    bracket_stack.pop()
                    nested_brackets += 1
        if not nested_brackets:
            return False
        else:
            return True
    else:
        return False


