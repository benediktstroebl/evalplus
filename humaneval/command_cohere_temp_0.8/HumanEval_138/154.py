```python
def is_equal_to_sum_even(n):
    even_nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    return n in even_nums
```

This function directly tests if the given number n is present in the list of positive even numbers. 

To ensure the function remains self-contained, the list of even numbers is explicitly defined within the function, allowing it to function independently without relying on any external variables or data.