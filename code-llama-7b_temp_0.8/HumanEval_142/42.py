


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
    # Initialize an empty list to hold the square and cubed integers.
    lst2 = []

    # For each element in lst.
    for i in range(len(lst)):
        if (i % 3 == 0 and (i + 1) % 3 != 0) or (i % 4 == 0 and (i + 1) % 4 != 0):
            # If the index of the element is a multiple of 3 but not a multiple of 4.
            lst2.append(lst[i] ** 2)
            # Square the element.

        elif (i % 4 == 0 and (i + 1) % 4 != 0) or (i % 3 == 0 and (i + 1) % 3 != 0):
            # If the index of the element is a multiple of 4 but not a multiple of 3.
            lst2.append(lst[i] ** 3)
            # Cube the element.

        else:
            # Otherwise, don't do anything.
            lst2.append(lst[i])

    # Sum the elements in lst2.
    sum_ = sum(lst2)

    return sum_

