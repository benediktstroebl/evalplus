
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

    # long version
    # brackets = []
    # for s in string:
    #     if s == '[':
    #         brackets.append(s)
    #     elif s == ']':
    #         if brackets:
    #             brackets.pop()
    #         else:
    #             return False
    # return True if brackets else False

    # short version
    return string.count('[') == string.count(']')

