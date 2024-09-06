
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
    count_brackets = 0
    for i in string:
        if i == '[' or i == '{' or i == '(' or i == '<':
            count_brackets += 1
        elif i == ']' or i == '}' or i == ')' or i == '>':
            if count_brackets == 0:
                return False
            else:
                count_brackets -= 1
    if count_brackets == 0:
        return True
    else:
        return False
