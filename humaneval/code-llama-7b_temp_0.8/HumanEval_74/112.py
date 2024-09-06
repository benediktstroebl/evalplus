
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
    # Create empty lists
    lst3 = []
    lst4 = []
    
    # Create empty variables
    count = 0
    
    # Create a for loop that iterates through lst1
    for i in lst1:
        # Iterate through each string in lst1
        for j in i:
            # If the string contains a number
            if j.isnumeric():
                # Increment count by 1
                count += 1
    
    # Repeat the process above for lst2
    for i in lst2:
        for j in i:
            if j.isnumeric():
                count += 1
    
    # Create an if-else statement to check if the count is greater than the length of lst1
    if count > len(lst1):
        # Return lst2
        return lst2
    # If not, return lst1
    else:
        return lst1
