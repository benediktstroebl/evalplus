
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

    
    bracket_dict = {'{' : '}', '[':']', '(':')'}

    brackets = []
    for i in string:
        if i in bracket_dict:
            brackets.append(i)
        elif len(brackets) == 0 or bracket_dict[brackets.pop()]!= i:
            return False
    
    return len(brackets) == 0


