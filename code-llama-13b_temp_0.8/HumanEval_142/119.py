


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
    # Store the index of the current element we're visiting
    index = 0
    
    # Create an empty list to store our answer
    # We won't add anything to our answer until the end. 
    # This is more efficient than adding to a list one-by-one
    # as we do not have to reallocate memory to add a new element
    # to our answer list. 
    answer = []
    
    # Iterate over the list
    while index < len(lst):
        # If we're at an index that's a multiple of 3
        if index % 3 == 0:
            # Add the current element to the answer list, squared
            answer.append(lst[index] * lst[index])
        # If we're at an index that's a multiple of 4
        if index % 4 == 0:
            # If the index is not also a multiple of 3
            if index % 3 != 0:
                # Add the current element to the answer list, cubed
                answer.append(lst[index] * lst[index] * lst[index])
        # Increase the index counter by 1
        index += 1
        
    # Return the sum of all elements in the answer list
    return sum(answer)
