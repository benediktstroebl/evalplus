
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
    # Get all brackets in the input string
    brackets = string.count('[') - 1
    # Get all possible nested brackets by iterating over all possible bracket positions
    nested_brackets = [string[i:i+2] for i in range(0, len(string), 2)]
    # Check if there is a valid subsequence of nested brackets
    for subsequence in nested_brackets:
        if len(subsequence) >= 2 and subsequence[-1] == subsequence[0] * -1:
            nested_brackets = [bracket[1:-1] for bracket in nested_brackets]
            if all(bracket in nested_brackets for bracket in subsequence):
                return True
    return False
