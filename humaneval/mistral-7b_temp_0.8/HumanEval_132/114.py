
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

    # Create a while loop
    # Inside the while loop,
    # - check if the current string starts with '[' or ']'
    # - if it starts with '[', then append it to a new list
    # - if it starts with ']', then pop the first item from the list
    # - if the current string is empty, then return True
    # - else, return False
    # In each iteration, check if the new string is still valid

    # An extra loop to check if the list is empty
    # If it is not empty, then return True
    # Else, return False

    # Create a while loop and iterate through the string
    # If the string starts with '[', append it to the new list
    # If the string starts with ']', pop the first item from the list
    # If the string is empty, return True
    # If the string is not empty, return False

    # Create a while loop and iterate through the string
    # If the string starts with '[', append it to the new list
    # If the string starts with ']', pop the first item
