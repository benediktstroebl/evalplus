
def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    """
    # Keep track of how many changes made
    changes = 0
    # Set a dictionary
    d = {}
    # Iterate over the array
    for num in arr:
        # If num is not in dictionary, add it as the key and set the value to 0
        if num not in d:
            d[num] = 0
        # Otherwise, add 1 to its value
        else:
            d[num] += 1
    # Set variables to count the number of elements in even and odd positions
    even = 0
    odd = 0
    # Iterate over the dictionary
    for value in d.values():
        # If the value is even, add 1 to the even counter
        if value % 2 == 0:
            even += 1
        # Otherwise add 1 to the odd counter
        else:
            odd += 1
    # If there are more odd elements than even elements, then make the difference of odd - even to the number of changes
    if odd > even:
        changes += odd - even
    # Else, make the difference of even - odd to the number of changes
    else:
        changes += even - odd
    # Return the number of changes
    return changes













