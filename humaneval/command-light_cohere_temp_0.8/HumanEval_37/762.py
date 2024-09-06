```python
def sort_even(l: list):
    return sorted(l, key=lambda x: (x if x % 2 == 0 else x + 1))

# Test the function
test_sort_even = []
test_sort_even.add([1, 2, 3)
test_sort_even.add([5, 6, 3, 4)
test_sort_even.add([5, 6, 5, 4)
test_sort_even.add([6, 5, 6, 4, 3)

# Call the function and compare the results
result = sort_even(test_sort_even)

assert len(result) == 4  # Check the length of the result is 4
assert [x for x in result if x == 3] == [3, 6, 5, 4]  # Check the sorted result matches the expected output

print("Success!")
```