
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
    def find_nesting(string):
        count = 0
        for i, character in enumerate(string):
            if character == '{':
                count += 1
            if character == '}':
                count -= 1
            if count < 0:
                return False
        if count == 0:
            return True
        return False
    return find_nesting(
