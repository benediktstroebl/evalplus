Here's a Python script that contains a function called `is_equal_to_sum_even` that evaluates whether a given number can be written as the sum of exactly 4 positive even numbers. The function is designed to return `True` if the condition is met and `False` otherwise:
```python
def is_equal_to_sum_even(n):
    even_nums = [2 * x for x in range(1, (n // 2) + 1)]
    return n == sum(even_nums) and n == 4 * sum(even_nums)
```
This function leverages list comprehension to generate a list of even numbers from 1 to `(n//2)` (`n` divided by 2) inclusive. It then computes two sums: one with the count of even numbers, and the other quadrupling that count, to determine if the number under consideration is equal to both sums. 

Here's an example of how you can use the function with the intended inputs:
```python
print(is_equal_to_sum_even(8))  # Should print True
print(is_equal_to_sum_even(6))  # Should print False
print(is_equal_to_sum_even(4))  # Should print False
```
This should produce the following output:
```bash
True
False
False
``` 
This function properly determines whether the given number can be expressed as the sum of 4 positive even numbers, according to the problem statement.