```python
def smallest_change(arr):
    arr = list(set(arr))
    return sum((x + 1) // 2 for x in range(1, len(arr) // 2 + 1) if arr[x - 1] != arr[-x] and arr[x] != arr[-x - 1])
```

The function uses a list comprehension to generate a list of all the indices of elements that are not symmetric around the middle of the array. It then counts the minimum number of changes required by adding the indices that are not between the same elements, then dividing by 2, accounting for the fact that each element can be changed once to any other element to make the array palindic. The result is that the function returns the smallest number of changes necessary to make the array palindic.

Here is a more detailed explanation of the code:
- The `arr = list(set(arr))` line removes all duplicate elements within the array, as a palindrome can be formed in multiple ways for arrays with duplicate elements.
- The line `return sum((x + 1) // 2 for x in range(1, len(arr) // 2 + 1) if arr[x - 1] != arr[-x] and arr[x] != arr[-x - 1])` uses a generator expression within the sum function to calculate the number of changes required for each index of the array where the element is not the same as its corresponding index in reverse. The sum of this result gives the total number of changes needed.
- The `if arr[x - 1] != arr[-x] and arr[x] != arr[-x - 1]` condition checks if the element at index `x` is not the same as the element at index `-x` (its corresponding index in the reverse order) and if the element at index `x` is also not the same as the element at index `(-x - 1)` (its corresponding index in the reverse order). This means that the condition only returns True for indices of elements that are not symmetric around the middle of the array, and therefore need to be changed to create a palindrome. 

This solution has a time complexity of `O(n)` where `n` is the length of the input array, due to the single pass through the array to determine the indices of elements that are not symmetric. It also has a space complexity of `O(1)` as it does not require any additional space.