
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
    # the idea is to use the stack to store open brackets
    # and then check if we have a matching closing bracket
    # for every new opening bracket
    # if we do not have a matching closing bracket we return false
    # if we do have a matching closing bracket we pop the top
    # element from the stack and check if the next element is also
    # a closing bracket (i.e. we are not dealing with an inner
    # nesting of brackets). if we are dealing with an inner
    # nesting of brackets we simply ignore the closing bracket
    # and continue checking for an outer closing bracket

    # example
    # input: '[[[]]]]'
    # the stack contains two opening brackets (i.e. ['['])
    # the first closing bracket we see is a matching bracket for the 
    # top element in the stack (i.e. ']')
    # so we pop the top element from the stack (i.e. ['[')
    # and we continue checking for an outer closing bracket (i.e.
