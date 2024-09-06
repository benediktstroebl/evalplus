
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    
    # make a new list
    new_list = []
    # check each item and add it to new list if it passes the filter
    for item in nums:
        if item > 10 and (item % 10) % 2 == 1:
            new_list.append(item)
    # return the number of items in the list
    return len(new_list)