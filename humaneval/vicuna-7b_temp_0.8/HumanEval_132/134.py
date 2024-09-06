
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
    def helper(string):
        if string == '':
            return True
        for i in range(len(string)-1):
            for j in range(i+1, len(string)):
                if string[i:j] == string[j:i+1] or string[i:j] == ']' in string[j:i+1] or string[j:i+1] == '[' in string[i:j]:
                    return False
        return True
    return helper(string)