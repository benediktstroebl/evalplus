
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

    def bracket(s):
        s_list = []
        for i in s:
            if i == '[':
                s_list.append(i)
            elif i == ']':
                if len(s_list) == 0:
                    return False
                s_list.pop()
            return True
        return True

    s_list = []
    for i in string:
        if i == '[':
            s_list.append(i)
        elif i == ']':
            if len(s_list) == 0:
                return False
            s_list.pop()
        return True
    return False




