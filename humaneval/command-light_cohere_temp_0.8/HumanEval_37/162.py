```python
def sort_even(lst):
    return lst[:] + [x for x in lst[1::2]] + lst[-1::-1]

# Test case 1
print(sort_even([1, 2, 3]))  # Expected output: [1, 2, 3]

# Test case 2
print(sort_even([5, 6, 3, 4]))  # Expected output: [3, 6, 5, 4]

# Test case 3
print(sort_even([3, 9, 8, 5, 2]))  # Expected output: [2, 3, 5, 8, 9]
```
The function `sort_even` takes a list as input and returns a new list that sorts even numbers in the first half of the original list, followed by sorting the odd numbers in the second half of the original list. The function uses the exact values of even and odd numbers, instead of sorting them numerically as the default behavior. The function returns the final list that is a sorted version of the original list.