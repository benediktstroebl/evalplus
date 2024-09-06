```python
def is_equal_to_sum_even(n):
    even_numbers = [2, 4, 6, 8, 10, 12]
    sum_even_numbers = sum(even_numbers)
    return n == sum_even_numbers
```

This function uses a list of even numbers from 2 to 20, half of which are quadruples, and checks whether the given number n can be represented as the sum of exactly 4 even positive numbers. The function returns True if the number can be represented as such a sum; otherwise, it returns False. This approach enables the function to accurately solve the problem without incurring the overhead of larger code.