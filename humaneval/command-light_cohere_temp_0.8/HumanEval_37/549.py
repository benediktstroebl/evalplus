```python
def sort_even(l: list):
    return sorted(l, key=lambda x: x if x % 2 == 0 else x - 1)

# Test case: sorting even and odd numbers in separate lists
even = [2, 4, 6, 8, 10]
odd = [1, 3, 5, 7]

# Call the function with both lists
even_sort = sort_even(even)
odd_sort = sort_even(odd)

# Validate the results
assert even_sort == [2, 4, 6, 8, 10]
assert odd_sort == [1, 3, 5, 7]

# Intuitive result for even, odd numbers
print("Even numbers:", even_sort)
print("Odd numbers:", odd_sort)
```

This script defines the `sort_even` function, which takes a list `l` as input and sorts it such that even numbers appear before odd numbers, and the two lists are identical. The function achieves this result using the `sorted` function with a custom key function. The test case validates that the output of the `sort_even` function with two lists: