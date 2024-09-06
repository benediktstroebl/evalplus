```python
def move_one_ball(arr):
    # If the array is empty, it's always possible to sort it in non-decreasing order
    if not arr:
        return True

    # Use a counter to keep track of the number of right shifts required to sort the array
    max_shifts = 0

    # Traverse the array and find the rightmost element
    for i in range(len(arr)-1, -1, -1):
        # Count shifts required for this element to get to index 0
        max_shifts = max(max_shifts, arr[i] - i)

    # Check if any element requires more than 1 shift, which would make the sorting impossible
    return max_shifts <= 1
```

The reasoning behind the approach is straightforward; if it's possible to sort the array by performing right shifts, the maximum number of shifts should not exceed 1 (because shifting an element beyond the array's length is undefined). So, we iterate through the array and calculate the maximum number of shifts required for any element to reach the 0th index. If this maximum count is 1 or less, the sorting is possible; otherwise, it's not. And, since this is a traversed array, we can do this in O(n) time, where 'n' is the length of the array. 

To test this, you can create a simple test case:
```python
test_case = [3, 5, 4, 1, 2]
print(move_one_ball(test_case))  # Expected output: False
``` 

This would follow the example provided in the problem statement, where the array [3, 4, 5, 1, 2] would require 2 right shifts, which is impossible, hence returning 'False'.