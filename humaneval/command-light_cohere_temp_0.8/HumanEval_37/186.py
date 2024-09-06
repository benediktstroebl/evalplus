```python
def sort_even(l: list):
    return sorted(l, key=lambda x: (x if x % 2 == 0 else x + 1))

# Test the function with markdown codes
test_sort_even = []
test_sort_even.add( [1, 2, 3])
test_sort_even.add(5, 6, 3, 4)

result = sort_even(test_sort_even)

assert result == [3, 6, 5, 4]
```