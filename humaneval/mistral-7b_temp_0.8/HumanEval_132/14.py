
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

    # ********** solution 1 ***********

    # return '[' in string and ']' in string

    # ********** solution 2 ***********

    for char in string:
        if char == '[':
            count = 1
            for x in string:
                if x == ']' and count > 0:
                    count -= 1
                elif x == '[':
                    count += 1
                if count == 0:
                    return True
    return False

