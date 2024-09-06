```python
def sort_even(lst):
    even_lst = [x for x in lst if x % 2 == 0]
    return even_lst

# Test cases
test_sort_even = []
test_lst = [5, 6, 3, 4]
test_sort_even.add(test_lst)
test_sort_even.add([1, 2, 3])
test_sort_even.add([5, 6, 4])

# Function call and checking
result = sort_even(test_lst)
print("Sorted even numbers:", result)

# Expected output: [3, 4, 5, 6]
```