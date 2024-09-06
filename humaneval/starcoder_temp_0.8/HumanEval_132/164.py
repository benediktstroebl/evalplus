
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
    # s_list = []
    # for char in string:
    #     s_list.append(char)
    # s_list = ''.join(s_list)
    # s_list = [char for char in s_list]
    # s_list = ''.join(s_list)
    s_list = ''.join(string)
    # print(s_list)
    nest_list = []
    nest_char = []
    for char in s_list:
        if char == '[':
            nest_char.append(char)
            nest_list.append(nest_char)
        elif char == ']':
            if not nest_list:
                return False
            else:
                nest_char.append(char)
                nest_list.append(nest_char)
                nest_char = []
                nest_list = nest_list[:-1]
    # print(nest_list)
    if nest_list:
        return True
    else:
        return False
