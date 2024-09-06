
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
    # This is a simple problem. Just loop through the string, and for every "[" encountered, increase
    # the bracket counter. For every "]" encountered, decrease the counter. If at the end the counter is
    # 0, return False.

    counter = 0
    for ch in string:
        if ch == '[':
            counter += 1
        elif ch == ']':
            counter -= 1
        if counter < 0:
            return False
    if counter > 0:
        return False
    return True

