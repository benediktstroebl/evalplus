
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
    if len(string) == 2:
        if string == '[]':
            return False
        else:
            return True
    else:
        start = 0
        end = 0
        while start < len(string) - 1:
            if string[start] == '[':
                end = start + 1
                while end < len(string) - 1:
                    if string[end] == ']':
                        end = end + 1
                        if string[end] == '[':
                            return True
                    else:
                        break
            start += 1
        return False
        

