
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
    def is_nested(string):
        string_arr = string.split('[')
        for i in range(len(string_arr)):
            if '[' in string_arr[i]:
                string_arr.pop(i)
        if len(string_arr) == 0:
            return True
        return False

    if is_nested(string):
        return True
    else:
        return False
