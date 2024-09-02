
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

    if string == '[]':
        return True
    for i in range(len(string)):
        if string[i] == '[':
            bracket = True
            new_string = string[i:]
            for j in range(len(new_string)):
                if new_string[j] == ']':
                    bracket = False
                    continue
                if new_string[j] == '[':
                    if bracket:
                        return True
                    else:
                        continue
                else:
                    continue
            if bracket:
                return True
    return False
