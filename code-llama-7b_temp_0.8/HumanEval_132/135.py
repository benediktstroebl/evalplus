
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

    def get_nest_level(string):
        return string.count('[') - string.count(']')

    if get_nest_level(string) == 0:
        return False
    else:
        nest_level = get_nest_level(string)
        for i in range(len(string)):
            sub_string = string[i:]
            if get_nest_level(sub_string) == nest_level:
                return True
            elif get_nest_level(sub_string) < nest_level:
                return False

