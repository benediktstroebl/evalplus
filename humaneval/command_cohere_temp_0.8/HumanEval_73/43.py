```python
def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    Returns:
        integer 
    """
    # create a counter to track the number of changes
    change = 0
    # initialize the first and last indices
    first, last = 0, len(arr) - 1
    # iterate through the array and at each step compare the current element to the element at the opposite end of the array
    while first < last:
        if arr[first] != arr[last]:
            change += 1
            # increment the index of the element that needs to be changed
            first += 1
            # decrement the index of the element at the opposite end
            last -= 1
        else:
            # if the element matches at the current indices, both indices closer towards the center of the array
            first += 1
            last -= 1
    return change
```

The function takes an array of integers as input and returns the minimum number of elements that need to be changed to make the array palindromic. The function first creates a counter to track the number of changes and initializes the first and last indices.

Then, it iterates through the array and at each step compares the current element to the element at the opposite end of the array. If the elements differ, it increments the change counter and increments the index of the element that needs to be changed, and decrements the index of the element at the opposite end. If the elements are the same, it increments both indices toward the center of the array.

This process continues until the first index is incremented past the last index, at which point the function returns the change counter.  The function handles cases where the array is already palindromic, as well as cases where one end of the array is match the opposite end, but the middle section is reversed. 

This is an efficient algorithm with a time complexity of O(n), where n is the length of the array, as it only requires a single pass through the array once, and has a constant additional space complexity for the counter variable.