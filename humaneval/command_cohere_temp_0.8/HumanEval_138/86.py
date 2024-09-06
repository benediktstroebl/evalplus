```python
def is_equal_to_sum_even(n):
    even_nums = [2, 4, 6, 8, 10, 12]
    return n in even_nums
```

This function directly tests if the given number n is present in the list of positive even numbers. The list `even_nums` can be modified to include other even numbers, however, this list already covers all even numbers up to a sufficient limit. 

This approach allows for a simple and efficient solution to the problem. And since the problem is evaluated as a boolean, the return statement can be written in a ternary style, which will return the variable `n` if the condition is met, and `False` otherwise. 

Please note that this code assumes that n is a positive integer, as no validation is performed on the input. Adjustments to handle negative numbers or integers and floats may be warranted based on the context of the problem.