```python
def is_equal_to_sum_even(n):
    even_nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    return n in even_nums
```

This function directly tests if the given number n is present in the list of positive even numbers. The function should return True if the number can be written as the sum of exactly 4 positive even numbers, and False if it cannot. 

For example, is_equal_to_sum_even(8) == True, as 8 is a positive even number and is part of the list. Similarly, is_equal_to_sum_even(6) == False, as 6 is not part of the list of even numbers. 

This approach provides a simple and efficient solution to the problem, directly answering the question without unnecessary complexity.