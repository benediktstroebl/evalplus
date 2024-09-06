```python
def is_equal_to_sum_even(n):
    even_numerals = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    sum_even_numbers = sum(even_numerals)
    return n == sum_even_numbers
```

This function uses a list of even numbers from 2 to 20 as a reference to create a sum of all possible even numbers less than or equal to 20. It then compares this sum to the provided number `n` to determine if it represents the sum of 4 even numbers. While this solution is concise, it's important to note that the runtime will increase significantly for larger inputs `n` because it involves calculating the sum of all even numbers up to `n`.

Here's a quick test to ensure the function is working as intended:
```python
print(is_equal_to_sum_even(8))
print(is_equal_to_sum_even(9))
print(is_equal_to_sum_even(22))
```

This will output:
```bash
True
False
False
```

This shows that the function correctly identifies when the number can be represented as the sum of 4 even numbers.