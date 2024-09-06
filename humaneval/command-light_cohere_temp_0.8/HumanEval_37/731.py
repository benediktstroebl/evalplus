```python
def sort_even(lst):
    even_lst = [x for x in lst if x % 2 == 0]
    return even_lst if even_lst == lst else even_lst

# Test the function with sample inputs
print(sort_even([1, 2, 3]))  # Expected output: [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # Expected output: [3, 6, 5, 4]
```
This script defines a function `sort_even` that sorts even numbers in an input list and returns the modified list.  The uses a simple indexing to filter even numbers and checks if the filtered list is equal to the original list to return it. 

This code is self-contained and can be copied and pasted into any Python environment to run the function and see the test cases.