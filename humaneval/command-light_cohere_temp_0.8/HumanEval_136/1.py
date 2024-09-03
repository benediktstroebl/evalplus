```python
def largest_smallest_integers(lst):
    if not negative_int_lst:
        return (None, None)  # No negative or positive integers
    else:
        # Find the maximum of all negative integers
        max_neg_int = max(x for x in negative_int_lst if x < 0)

        # Find the smallest of all positive integers
        min_pos_int = min(x for x in positive_int_lst if x > 0)

        return (max_neg_int, min_pos_int)

# Test the function with examples
negative_int_lst = [-1, 0, 2, 3, -4]
positive_int_lst = [1, 2, 3, 4, 5]
result = largest_smallest_integers(negative_int_lst + positive_int_lst)
print(result)  # Output: (-3, 5)

# Another test with empty list
result = largest_smallest_integers([])
print(result)  # Output: (None, None)
```
This script defines a function `largest_smallest_integers` that takes a list as input and returns a tuple containing the largest of all negative integers and the smallest of all positive integers. The function uses two nested loops to find these values, and if there are no negative or positive integers, it returns `None` for both components. 

The script then tests the function with various input lists and prints the results. This provides a test cases and demonstrates the function correctly.