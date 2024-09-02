
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
    def helper(left, right):
        if left == '[]' or right == '[]':
            return True
        if left != right and left == '[':
            return helper(right, left[1:])
        if right != left and right == '[':
            return helper(left, right[1:])
        return False
    return helper(string[0], string[-1])
