
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
    # 1. if string length is 0, return False
    # 2. if string length is 1, return False
    # 3. check if there are any consecutive square brackets
    # 4. if there are, check if any are nested.
    # 5. if any are nested, return True, else False
    # 6. if not, return False
    if len(string) == 0:
        return False
    if len(string) == 1:
        return False

    for i in range(len(string)):
        if string[i] == '[':
            if string[i+1] == ']':
                return False
            elif string[i+1] == '[':
                for x in range(i+2, len(string)):
                    if string[x] == ']' and string[x+1] == ']':
                        return True
    return False

