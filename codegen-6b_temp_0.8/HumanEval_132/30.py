
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
    def recur(index, count):
        if count == n: return True
        if index == n: return False
        if string[index] == '[' and recur(index + 1, count):
            return True
        if string[index] == ']' and recur(index + 1, count + 1):
            return True
        return False

    if len(string) == 0: return False
    if len(string) == 1: return False
    if string.count('[') != string.count(']'): return False
    n = len(string)
    return recur(0, 0)

    # sol2
    def is_nested1(string):
        return True if string.count('[') - string.count(']') >= 0 else False
    return True if not string or is_nested1(string) else False

