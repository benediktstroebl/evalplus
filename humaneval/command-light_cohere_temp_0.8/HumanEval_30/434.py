```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test case 1: Returns a list of positive numbers from a list of integers
# Test case 2: Returns an empty list if input list is empty
# Test case 3: Returns a list of numbers from a list of strings (With mixed case)
get_positive([1, 2, 3, -4, 4, 5])
get_positive([5, -3, 3, "abc", 0, "one", 1])
get_positive([])
```
This script defines a function get_positive that takes a list as input and returns a list of positive numbers from that list. 

The function uses list comprehension with the condition num >= 0 to filter out the positive numbers from the list. 

The test cases include passing the function with a list of integers, an empty list, a list of strings, and various edge cases.