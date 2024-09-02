
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

    
    def get_num(string):
        return string.count('[') - string.count(']')
    
    def check(string):
        string = string.replace(']', '] ')
        arr = string.split()
        arr = [i for i in arr if i.startswith('[') and i.endswith(']')]
        return get_num(string) == sum(get_num(i) for i in arr)
    
    return check(string)

