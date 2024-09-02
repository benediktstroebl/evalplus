
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
    def has_nested(string):
        open_brackets = ['[' , '{' , '(']
        close_brackets = [']' , '}' , ')']
        bracket_stack = []
        for char in string:
            if char in open_brackets:
                bracket_stack.append(char)
            elif char in close_brackets:
                if not bracket_stack:
                    return False
                bracket_stack.pop()
        if not bracket_stack:
            return True
        else:
            return False
    return has_nested(string)



