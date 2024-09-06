
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
    
    # first, create a function to add up the length of a list
    def sum_chars(lst):
        # create a variable to hold the length of each string in the list
        total = 0
        # iterate over the list
        for item in lst:
            # for each item, add the length of each string to the variable
            total += len(item)
        # return the total
        return total
    
    # create a variable to hold the sum of chars in the first list
    total1 = sum_chars(lst1)
    # create a variable to hold the sum of chars in the second list
    total2 = sum_chars(lst2)
    # if the first total is less than the second total, return the first list
    if total1 < total2:
        return lst1
    # if the second total is less than the first total, return the second list
    elif total2 < total1:
        return lst2
    # if the two totals are the same, return the first list
    else:
        return lst1
