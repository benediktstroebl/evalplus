
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
    # I'm thinking that there must be some other test case that needs to be addressed.
    # If so, let me know.
    brackets = {
        ']': '[',
        ')': '(',
        '}': '{'
    }

    counter = 0
    for char in string:
        if char in brackets.values():
            counter += 1
        elif char in brackets.keys():
            counter -= 1
            if counter < 0:
                return False
    return True if counter == 0 else False

