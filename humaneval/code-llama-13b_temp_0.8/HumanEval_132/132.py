
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
    new_string = string.replace('][', '] [')
    # print(new_string)
    list_of_string = new_string.split()
    # print(list_of_string)
    len_string = len(list_of_string)
    # print(len_string)
    # print(list_of_string)
    nested_flag = False
    for i in range(len_string):
        # print(list_of_string[i])
        if list_of_string[i][0] == '[' and list_of_string[i][-1] != ']':
            nested_flag = True
    return nested_flag

