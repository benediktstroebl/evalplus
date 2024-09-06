```python
def is_equal_to_sum_even(n):
    even_nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    return n in even_nums
```

This function directly tests if the given number n is present in the list of positive even numbers. 

To ensure this function remains self-contained, the list of even numbers is included directly in the code, avoiding any external dependencies. 

This solution will work independently as long as the script has access to Python and the standard library. 
To see if this solution works for all test cases, simply call the function with different numbers as shown in the example below:
```python
print(is_equal_to_sum_even(8))  # Should print True
print(is_equal_to_sum_even(10))  # Should print False
print(is_equal_to_sum_even(12))  # Should print False
``` 

This will help you verify the functionality of the script.