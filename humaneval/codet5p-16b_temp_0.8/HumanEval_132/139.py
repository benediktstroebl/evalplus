
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

    def check_valid(string):
        stack = []
        for bracket in string:
            if bracket == '[':
                stack.append(bracket)
            elif bracket == ']':
                if len(stack) == 0:
                    return False
                else:
                    stack.pop()
        if len(stack) == 0:
            return True
        return False
    
    def nested(string):
        if len(string) == 0:
            return True
        if string[0] == '[':
            return nested(string[1:])
        else:
            return nested(string[1:])
    
    return check_valid(string) and nested(string)
