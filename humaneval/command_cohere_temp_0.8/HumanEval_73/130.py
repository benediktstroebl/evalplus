```python
def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    Returns:
        int: The minimum number of changes required
    """
    # Ensure the array contains only unique integers
    arr = list(set(arr))
    # Create a reversed copy of the array
    rev = arr[::-1]
    # Calculate the absolute difference between the two arrays
    diff = [abs(x-y) for x, y in zip(arr, rev)]
    # Return the count of non-zero diffs, as zeros represent elements that are already in the correct position
    return sum(1 for x in diff if x)
```

The solution hinges on understanding that a palindrome requires symmetric elements, where the absolute difference between any two corresponding elements must be zero. Non-zero differences indicate elements that need to be changed to achieve symmetry. The code iterates through each element, subtracting one from the counter for every non-zero difference. Finally, the total count of changed elements is returned. 

To ensure correctness and account for cases such as duplicate elements, the code first converts the input array to a list of unique elements. This step guarantees there are no duplicate elements in the array. Then, the list is reversed and comparisons are performed using the `zip` function. It's worth noting that this approach has a time complexity of O(n log n) due to the use of set comprehension, which has a logarithmic time cost for converting the list to a set. However, this is justified as it makes the problem and its solution more efficient and readable.