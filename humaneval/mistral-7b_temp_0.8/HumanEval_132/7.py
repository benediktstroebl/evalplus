
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

    list_of_brackets = list(string)
    count_brackets = 0
    result = True
    for index, bracket in enumerate(list_of_brackets):
        if bracket == '[':
            count_brackets += 1
        elif bracket == ']':
            count_brackets -= 1
        if count_brackets < 0:
            result = False
    return result




