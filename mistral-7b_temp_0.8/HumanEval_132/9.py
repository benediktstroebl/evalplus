
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
    opening_bracket = "["
    closing_bracket = "]"
    string_list = list(string)
    opening_count = 0
    closing_count = 0
    for char in string_list:
        if char == opening_bracket:
            opening_count += 1
        else:
            closing_count += 1
        if opening_count < closing_count:
            return True
    return False
