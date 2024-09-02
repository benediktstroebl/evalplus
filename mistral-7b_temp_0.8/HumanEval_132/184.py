
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
    if string == '':
        return False
    if string[0] != '[':
        return False
    string = string[1:-1]
    print(string)
    if not string:
        return True
    first_bracket = string.find('[')
    if first_bracket == -1:
        return False
    second_bracket = string.find(']')
    if second_bracket == -1:
        return False
    if first_bracket == second_bracket:
        return False
    return is_nested(string[:first_bracket] + string[second_bracket+1:])
