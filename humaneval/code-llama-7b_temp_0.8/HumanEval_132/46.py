
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
    # my solution
    return "[" in string and "]" in string and string.index("]") > string.index("[")

    # solution 1
    # if "[" in string and "]" not in string:
    #     return True
    # elif "[" not in string and "]" in string:
    #     return True
    # elif not "[" in string and not "]" in string:
    #     return False

    # start = 0
    # end = 0
    # for i in string:
    #     if i == "[":
    #         start += 1
    #     if i == "]":
    #         end += 1
    # if start != end:
    #     return False
    # if start == 0 and end == 0:
    #     return False
    # if start > 0 and end > 0:
    #     return True
