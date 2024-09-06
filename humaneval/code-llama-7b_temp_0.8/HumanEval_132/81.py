
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
    # Analyse string
    # If there is no '[', return False
    if string.find('[') == -1: return False
    # If there is a ']', return True
    if string.find(']') > -1: return True
    # If there are brackets but no matching pair of brackets, return False
    if string.count('[') > string.count(']'): return False
    # If there are matching brackets but no nested brackets, return False
    if string.count('[]') == string.count('[[]') and string.count('[]') > 0: return False
    # If there is at least one nested bracket, return True
    else: return True
