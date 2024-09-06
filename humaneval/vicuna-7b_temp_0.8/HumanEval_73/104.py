
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
    # Create a dictionary to count how many times each element appears in the array
    count = {element: arr.count(element) for element in arr}

    # Create a list to keep track of the number of elements that need to be changed
    change = 0

    # Find the maximum value in the dictionary
    max_value = max(count.values()) + 1

    # Loop through the array and find the minimum number of elements that need to be changed
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            # If the current element is a palindrome, we can change any of the surrounding elements
            if arr[j] == arr[i]:
                change -= 1
                break
            # If the current element is not a palindrome, increment the change count
            else:
                change += 1
                if count[arr[i]] > count[arr[j]]:
                    change += 1

    # Return the minimum number of elements that need to be changed
    return change