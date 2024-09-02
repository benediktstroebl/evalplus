
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
    # Use a dictionary to track if we've seen any open brackets
    # We start with an empty dictionary
    open_brackets = {}
    
    # Use a set to track if we've seen any nested brackets
    # We start with an empty set
    nested_brackets = set()
    
    for char in string:
        # If we've seen an open bracket before and the current character is a ']',
        # we add the current string to the nested_brackets set
        if char in open_brackets and string[open_brackets.index(char) + 1] == ']':
            nested_brackets.add(string[open_brackets.index(char) + 1:])
            open_brackets.pop(open_brackets.index(char), None)
            
    # If there are any nested brackets in the string, return True
    return len(nested_brackets) > 0
