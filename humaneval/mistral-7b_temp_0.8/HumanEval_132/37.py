
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
    # Find the number of right brackets
    right_count = string.count("]")
    # Find the number of left brackets
    left_count = string.count("[")
    # Check if there is a single left bracket and single right bracket
    if left_count == 1 and right_count == 1:
        return True
    # Check if there is any left bracket left unmatched
    elif left_count > right_count:
        return False
    # Check if there is any right bracket left unmatched
    elif left_count < right_count:
        return False
    # Check if there are more than 2 right brackets without left brackets
    elif left_count == 0 and right_count > 2:
        return False
    # Check if there are more than 2 left brackets without right brackets
    elif left_count > 2 and right_count == 0:
        return False
    # Check if there are more than 2 left brackets without right brackets
    elif left_count > 2 and right_count >
