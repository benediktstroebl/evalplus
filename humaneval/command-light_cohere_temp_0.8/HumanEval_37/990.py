```python
def sort_even(lst):
    even_list = [x for x in lst if x % 2 == 0]
    return [x for x in even_list]

# Test cases
test_sort_even = []
test_sort_even.push_from_list([1, 2, 3])
test_sort_even.push_from_list([5, 6, 3, 4])

assertEqual(sort_even(test_sort_even), [1, 2, 3])

test_sort_even.push_from_list([5, 6, 3, 4])

assertEqual(sort_even(test_sort_even), [3, 6, 5, 4])

test_sort_even.push_from_list([5, 6, 7, 8])

assertEqual(sort_even(test_sort_even), [6, 5, 7, 8])
```

This code defines a function **`sort_even`** that takes a list and returns a new list with elements from the original list that are even indices. The returned list is sorted in ascending order, maintaining even indices. This allows us to sort lists of even numbers in a natural way, while ensuring the original even elements remain in place. 

Remember to include the backticks and indentation for readability.