```python
def sort_even(lst):
    return lst[:] + [x for x in lst[1:] + [0] * len(lst[0])] if x % 2 != 0]

# Test cases
test_sort_even = []
for i in range(10):
    test_sort_even.append([2, i, i+1])

# Validate function
def validate_sort_even(func):
    test_sort_even.validate(func(test_sort_even))
    return True

validate_sort_even(sort_even)
```
Do you want to sort even numbers in a list? We can solve this problem by creating a custom function that takes a list as input and returns a new list with even numbers sorted. The list's odd elements remain in the original order. We can achieve this up by adding the even numbers to the beginning of the list and then appending the remaining elements, which include the odd numbers and zeros. The result is a list with even numbers sorted.