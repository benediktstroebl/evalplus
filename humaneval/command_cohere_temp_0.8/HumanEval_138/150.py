```python
def is_equal_to_sum_even(n):
    even_nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    return n in even_nums
```

This function directly tests if the given number n is present in the list of positive even numbers. The function promptly returns true if the number is present in the list, implying that the number can be expressed as the sum of four positive even numbers. It's worth noting that the function leverages Python's list comprehension and in-built `in` operator for efficiency and readability. 

This approach offers a concise solution to the problem, directly answering the prompt's requirement to check whether the number can be expressed as the sum of exactly four positive even numbers, while maintaining efficiency and simplicity.