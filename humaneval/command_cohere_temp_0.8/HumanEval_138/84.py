```python
def is_equal_to_sum_even(n):
    even_nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    return n in even_nums
```

This function directly tests if the given number n is present in the list of positive even numbers. The function returns True if the number can be divided by 2 without leaving a remainder, which satisfies the condition of the problem.

To test this function, you can use the following loop:
```python
listed_numbers = [4, 6, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for n in listed_numbers:
    assert is_equal_to_sum_even(n) == n in even_nums
```

This block of code lists all the numbers from 4 to 20 and checks whether the function's output corresponds correctly to the specified condition.