```python
def move_one_ball(arr):
    # If the array is empty, it is always possible to sort it in non-decreasing order
    if not arr:
        return True

    # Use a counter to keep track of the number of right shifts required to sort the array
    max_shifts = 0

    # Traverse the array and find the rightmost element
    for i in range(len(arr)-1, -1, -1):
        # If the element is greater than the element on its left, increase the counter by 1
        if arr[i] > arr[i-1]:
            max_shifts += 1

    # If the maximum number of right shifts is odd, it is possible to sort the array in non-decreasing order
    return max_shifts % 2 == 0
```

This approach uses a clever algorithm to determine if it is possible to sort the array by moving just one ball. The algorithm traverses the array from right to left, counting the number of times it finds a larger element on the right side of the array. If this count is even, it is possible to rearrange the array by moving just one ball. Otherwise, if the count is odd, it will require two balls to move and the answer will be False. This algorithm has a time complexity of O(n), where n is the length of the input array `arr`.