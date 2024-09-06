


def sum_squares(lst):
    """"
    This function will take a list of integers. For all entries in the list, the function shall square the integer entry if its index is a 
    multiple of 3 and will cube the integer entry if its index is a multiple of 4 and not a multiple of 3. The function will not 
    change the entries in the list whose indexes are not a multiple of 3 or 4. The function shall then return the sum of all entries. 
    
    Examples:
    For lst = [1,2,3] the output should be 6
    For lst = []  the output should be 0
    For lst = [-1,-5,2,-1,-5]  the output should be -126
    """

    # so our goal here is to take a list of integers and add the sum of the squares of the numbers at indices that are multiples of 3, and the cubes of the numbers at indices that are multiples of 4 but not 3

    # first we are going to need to loop through our list and keep track of what indices are multiple of 3 and 4

    # we can loop through a list using the "for" loop syntax.  For each item in the list, we can do something

    # let's start by looping through the list and keep track of what indices are multiples of 3
    squared_multiples_of_3 = []
    for index, item in enumerate(lst):
        # what is the current index and what is the current item in the list
        # we are going to keep track of all the items that are multiples of 3
        if index % 3 == 0:
            squared_multiples_of_3.append(item)

    # now we want to keep track of the indices that are multiples of 4 but not 3
    
