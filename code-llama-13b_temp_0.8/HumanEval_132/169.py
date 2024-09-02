
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
    def search(sub):
        open_bracket = 0
        for b in sub:
            if b == '[':
                open_bracket += 1
            else:
                open_bracket -= 1
            if open_bracket < 0:
                return False
        return open_bracket > 0
    
    bracket_dict = {'[':']'}
    for i in range(len(string)):
        if string[i] == '[':
            for j in range(i+1, len(string)):
                if string[j] in bracket_dict[string[i]]:
                    if search(string[i+1:j]):
                        return True
    return False
