```python
def by_length(arr):
    sorted_arr = sorted(arr)[::-1]
    transf_map = {'1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', 
                  '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine'}
    result = [transf_map[str(num)][0] for num in sorted_arr if str(num) in transf_map]
    return result if result else []
```

The Python script solves the problem using the following steps:
1. Sort the array of integers from 1 to 9 in reverse order using the `sorted` function and `[::-1]` slice.
2. Create a translation map to replace each digit with its corresponding name.
3. Use a list comprehension to transform each digit into its name and include it in the result only if the digit is within the specified range.
4. Return an empty list if the input array is empty.

This solution has a time complexity of `O(n log n)` due to the sorting step and an auxiliary space complexity of `O(1)` as it only uses variables and constants for operations.