
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
    # nested = []
    # is_nest = False
    # for i in string:
    #     if i == "]":
    #         if len(nested) > 0:
    #             is_nest = True
    #             break
    #     else:
    #         nested.append(i)

    # print(is_nest)
    # return is_nest

    return any(is_nested(sub_string) for sub_string in string.split(']'))

