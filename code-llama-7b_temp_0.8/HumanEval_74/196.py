
def total_match(lst1, lst2):
    '''
    Write a function that accepts two lists of strings and returns the list that has 
    total number of chars in the all strings of the list less than the other list.

    if the two lists have the same number of chars, return the first list.

    Examples
    total_match([], []) ➞ []
    total_match(['hi', 'admin'], ['hI', 'Hi']) ➞ ['hI', 'Hi']
    total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) ➞ ['hi', 'admin']
    total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) ➞ ['hI', 'hi', 'hi']
    total_match(['4'], ['1', '2', '3', '4', '5']) ➞ ['4']
    '''
    # Create a function that returns the length of a string
    def word_length(lst):
        length = 0
        for i in lst:
            length += len(i)
        return length
    
    # Create a function that returns True if the lengths of each string are equal
    def compare_length(lst1, lst2):
        return (word_length(lst1) == word_length(lst2))
    
    # Create a function that returns True if the lengths of each string are greater than the other
    def compare_greater(lst1, lst2):
        return (word_length(lst1) > word_length(lst2))
    
    # Use the above functions to solve the problem
    if len(lst1) == len(lst2):
        return lst1
    elif compare_length(lst1, lst2):
        return lst2
    elif compare_greater(lst1, lst2):
        return lst1
    else:
        return lst2

