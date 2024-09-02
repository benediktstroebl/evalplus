
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
    def recur(string, count, s=0):
        if count == 0 and s == 0:
            return False
        if string[count] == ']':
            s += 1
            return recur(string, count - 1, s)
        return recur(string, count - 1, s)
    return recur(string, len(string) - 1)
    

