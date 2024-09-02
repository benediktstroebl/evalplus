
def search(lst):
    '''
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
    zero, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    Examples:
        search([4, 1, 2, 2, 3, 1]) == 2
        search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
        search([5, 5, 4, 4, 4]) == -1
    '''
    # I want to count each item, then sort by count.
    # If the count is less than or equal to the item, then return the item
    # If the count is greater than the item, return the count
    # I don't need a list of counts, I just need a count per item
    # I can count each item as I sort it, if I count it once I won't count it again
    # Do I want to keep the count in the list with the item?
    # I can just sort by count instead of sorting, and counting.
    # I can return the count for the last item.
    # The only case where this won't work is if the item and count are the same.
    # I need to sort the item and count separately
    # I can sort the item, then add the count to the item.
    # I'll add the count as a string to the item.
    # If the count is greater than the item, return the item
    # If the count is less than or equal to the item, return the item

    # SOLUTION 1
    # O(n
