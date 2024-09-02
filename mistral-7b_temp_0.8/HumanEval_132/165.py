
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

    open_brackets = '['
    close_brackets = ']'

    new_str = ""
    for char in string:
        if char in open_brackets:
            new_str += char
        elif char in close_brackets:
            if new_str:
                new_str = new_str[:-1]
            else:
                new_str += char
        else:
            new_str += char

    return len(new_str) > 0




