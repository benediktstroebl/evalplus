
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

    # Calculate the sum of the values in the list
    sum_of_elements = sum(arr)
    # Divide the sum by 2, if the sum is even there will be no centre element.
    # If the sum is odd we want the round down version of sum / 2
    centre = sum_of_elements // 2
    # If the sum is odd, add 1 so that we can include the centre value.
    centre = (sum_of_elements // 2) + (sum_of_elements % 2)
    # Initialise an array to contain the counts of each element, from 0 upwards
    element_count = [0 for i in range(100)]

    # Populate the element_count array with the counts of each element
    for element in arr:
        element_count[element] += 1

    # Initialise a counter to keep track of the elements we will need to change
    element_changes = 0
    # Loop through all elements of the array
    for i in range(100):
        # If the number of elements is more than the number needed to make it a palindrome
        if element_count[i] > centre:
            # Subtract the number of elements from the centre
            centre = centre - element_count[i]
        # If the number of elements is less than the number needed to make it a palindrome
        elif element_count[i] < centre:
            # Add the number of elements from the centre
            centre = centre - element_count[i]
            # Increment the count of elements we need to change
            element_changes += (centre - element_count[i])

    return element_changes

