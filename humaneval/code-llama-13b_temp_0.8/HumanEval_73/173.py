
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
    l = len(arr)
    # Check if list is empty
    if l == 0:
        return 0
    # Check if the list has only one element
    if l == 1:
        return 0

    # Create the list of starting with an empty list
    start = []

    # Create a list of the end
    end = []

    # Create a counter of the total of changes
    total = 0

    # If there is only two elements left
    if l == 2:
        if arr[0] == arr[1]:
            return 0
        else:
            return 2

    # Get the first half of the list
    for i in range(l // 2):
        start.append(arr[i])

    # Get the second half of the list
    for j in range(l // 2, l):
        end.append(arr[j])

    # Compare each element in the first and second half of the list
    for k in range(len(start)):
        # If the element in the first half is not the same as the element in the second half
        if start[k] != end[k]:
            start[k] = end[k]
            # Add one to the counter
            total += 1

    # If the first and second half are equal
    if start == end:
        return 0

    return total
