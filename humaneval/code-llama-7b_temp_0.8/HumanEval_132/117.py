
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
    import re

    # since the square brackets are closed/open we can just count the number of
    # opening and closing brackets and if the difference is more than one then
    # we know there is a nested square bracket
    bracket_count = len(re.findall('\[', string)) - len(re.findall('\]', string))
    return bracket_count > 1

