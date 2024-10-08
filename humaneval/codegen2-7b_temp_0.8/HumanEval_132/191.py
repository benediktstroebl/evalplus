
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
    brackets_dictionary = {
        '{': '}',
        '[': ']',
        '(': ')'
    }
    if not string:
        return False
    stack = []
    for bracket in string:
        if bracket in brackets_dictionary.keys():
            stack.append(bracket)
        else:
            if not stack:
                return False
            else:
                opening = stack.pop()
                if brackets_dictionary[opening]!= bracket:
                    return False
    return not
