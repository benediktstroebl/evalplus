
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

    bracket_list = []
    brackets = {'[':']', '{':'}', '(':')'}
    for bracket in string:
        if bracket in brackets:
            bracket_list.append(bracket)
        if bracket in brackets.values():
            if not bracket_list:
                return False
            last_bracket = bracket_list.pop()
            if brackets[last_bracket]!= bracket:
                return False
    return not bracket_list
