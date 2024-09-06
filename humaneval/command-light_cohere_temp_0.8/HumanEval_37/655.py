```python
def sort_even(lst):
    even_set = set(lst[1::filter(lambda x: x % 2 == 0)])
    return [x for x in lst if x in even_set]

# Test case: returns the list with even numbers sorted
test_sort_even = [5, 6, 3, 4]
sorted_even = sort_even(test_sort_even)
print(sorted_even)  # expected output: [3, 4, 5, 6]
```