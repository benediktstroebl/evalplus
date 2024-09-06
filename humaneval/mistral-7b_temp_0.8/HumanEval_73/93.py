
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

    # Convert the array to a set so we can remove duplicate values
    arr_set = set(arr)

    # Initialize the count to zero
    count = 0

    # Iterate through the set
    for i in arr_set:
        # Iterate through the array
        for j in arr:
            # If the current element is not the same as the set element
            if i != j:
                # Check if the element is the same as the set element's reversed value
                if i + j == j + i:
                    # If the elements are not the same, increase the count by one
                    count += 1

    # Return the count
    return count
