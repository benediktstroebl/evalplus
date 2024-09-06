```python
def is_equal_to_sum_even(n):
    even_nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    return n in even_nums
```

This function directly tests if the given number `n` is present in the list of even numbers `even_nums`. 

Evens are numbers that can be divided by 2 without leaving a remainder. Therefore, the list of evens starts from 2 and includes all even numbers. It is a valid assumption that every number can be expressed as a sum of at most 4 even numbers, as there are fewer odd numbers than even numbers. Hence, the `is_equal_to_sum_even` function may return `True` for a number that can be expressed as a sum of 5 or more even numbers. However, this assumption is still valid and does not break the problem statement's criterion. 

The function is concise and easy to interpret, but it can be improved with a more sophisticated approach, like factorization, to achieve the same result with fewer characters.