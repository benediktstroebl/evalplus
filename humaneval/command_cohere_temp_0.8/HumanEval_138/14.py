Here's a Python script that contains a function called `is_equal_to_sum_even` that solves the problem you've described:
```python
def is_equal_to_sum_even(n):
    even_nums = [2 * x for x in range(1, int(n**0.5) + 1) if x % 2 == 0]
    return len(even_nums) == 4 and n == sum(even_nums)
```
This function uses a list comprehension to generate all positive even numbers from 2 to the square root of n, and then checks whether the length of this list is exactly 4 and whether the list's sum is equal to n. The function returns True if both conditions are met, and False otherwise.

To test this function, you can uncomment the test cases and modify them as needed:
```python
# Test cases
print(is_equal_to_sum_even(8))  # Should print True
print(is_equal_to_sum_even(6))  # Should print False
print(is_equal_to_sum_even(4))  # Should print False
``` 
Let me know if you need anything else!