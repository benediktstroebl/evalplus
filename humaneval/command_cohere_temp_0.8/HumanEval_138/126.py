```python
def is_equal_to_sum_even(n):
    even_nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    return n in even_nums
```

This function directly tests if the given number n is present in the list of positive even numbers. Evidently, if a number is the sum of 4 even numbers, then it must be one of the numbers in the aforementioned list, since these are the only valid options for the 4 positive even numbers whose sum equals the number. Hence, this function directly answers the problem statement in a straightforward manner, without the need for any additional variables or complex operations.