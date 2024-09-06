
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
    brackets = []
    for character in string:
        if character == ']':
            if len(brackets) == 0:
                return False
            if brackets[-1] == '[':
                brackets.pop()
            else:
                return False
        elif character == '[':
            brackets.append(character)
    return len(brackets) == 0
