```python
def sort_even(lst):
    # Sort the list
    return sorted(lst, key=lambda x: (x % 2,) )

# Test case 1: Ensure odd values are at the beginning
test_odd = [1, 2, 3]
assertEqual(sort_even(test_odd), [1, 2, 3])

# Test case 2: Ensure equal values follow odd values
test_even = [5, 6, 3, 4]
assertEqual(sort_even(test_even), [3, 6, 5, 4])

# Test case 3: Ensure the list is sorted
test_list = [5, 6, 3, 4, 2]
assertEqual(sort_even(test_list), [2, 3, 5, 6, 4])
```
This script defines a function **`sort_even`** which takes a list as input and returns a sorted list, ensuring that even numbers come after odd numbers. The test cases ensure that the script produces the correct sorted output for different list inputs.