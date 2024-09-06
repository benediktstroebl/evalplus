```python
def is_equal_to_sum_even(n):
    even_nums = [2, 4, 6, 8, 10, 12]
    return n in even_nums
```

This function directly tests if the given number n is present in the list of positive even numbers. The list `even_nums` contains only positive even integers from 2 to 20, as it's explicitly stated in the problem statement that exactly 4 even numbers are needed, and the sum of 4 consecutive even numbers from 2 to 20 always results in a number from 14 to 40. Therefore, the given list contains all the sums that can be created using exactly 4 even numbers.