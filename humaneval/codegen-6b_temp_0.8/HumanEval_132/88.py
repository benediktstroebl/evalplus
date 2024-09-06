
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
    ans = False
    for i in xrange(0,len(string)):
        if string[i] == '[':
            ans = True
        elif string[i] == ']':
            ans = False
        if ans == True:
            if char_is_opening(string[i]):
                stack = 1
                j = i+1
                while stack != 0 and j < len(string):
                    if char_is_opening(string[j]):
                        stack += 1
                    elif char_is_closing(string[j]):
                        stack -= 1
                    j += 1
                if stack == 0:
                    return True
    return False
