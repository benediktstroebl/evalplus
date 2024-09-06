
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
    def matcher(i):
        list_status = []
        if i == len(string): return True
        if string[i] == '[' or string[i] == '(' or string[i] == '{':
            list_status.append(string[i])
            if is_nested(string):
                return True
            else:
                list_status.pop()
        return False
    return matcher(0)


