
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
    def count_open_brackets(string):
        count = 0
        for letter in string:
            if letter == ']':
                count += 1
        return count
    
    def check_nested(string):
        count = count_open_brackets(string)
        count -= 1
        if count > 0:
            return False
        else:
            return True
    
    if check_nested(string):
        return True
    elif count_open_brackets(string) == 0:
        return True
    else:
        return False

