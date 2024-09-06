```python
def smallest_change(arr):
    arr = list(set(arr))
    return sum([1 for i in range(len(arr)) if arr[i] != arr[-(i+1) % len(arr)]]);
```
This function works by first removing all duplicates from the input array using the 'set' method, then checks if an array is palindromic by checking if the first element is equal to the last element, and all the elements in between are also equal. 

To make the array palindromic, we just need to change the elements that are not equal to their corresponding positions in reverse order. Therefore, the number of changes is equal to the number of elements that are not equal to their corresponding positions. The 'sum' function together with a generator expression will iterate through the array and count the number of changes needed, outputting the minimum number of changes needed to make the array palindromic.

Here is a test case that can be used to verify the function:
```python
test_cases = [
    ([1, 2, 3, 5, 4, 7, 9, 6], 4),
    ([1, 2, 3, 4, 3, 2, 2], 1),
    ([1, 2, 3, 2, 1], 0),
    ([1, 2, 3], 0),
    ([1, 2], 1),
    ([1], 2),
    ([], 0)
]

for arr, expected in test_cases:
    assert smallest_change(arr) == expected
```
For each test case, the function `smallest_change()` is called with the respective input array and is checked whether the returned result is equal to the expected value.  If all assertions pass, it means the function is correct. 

Note that this solution runs in O(n) time complexity, where n is the length of the input array. This is because it only iterates through the array once to calculate the edits required, and performs no additional expensive operations.  This is a efficient approach for this problem.