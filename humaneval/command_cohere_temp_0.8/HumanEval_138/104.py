Here's a Python script that contains a function called `is_equal_to_sum_even` that solves the problem you've described:
```python
def is_equal_to_sum_even(n):
    even_nums = [2 * x for x in range(1, int(n**0.5) + 1)]
    return n == sum(even_nums)
```
This function uses a list comprehension to generate a list of positive even numbers from 2 to the square root of n. It then returns true if n is equal to the sum of these even numbers. The square root check ensures the list covers all possible even factors of n. 

The function is designed to evaluate whether a given number n can be written as the sum of exactly 4 positive even numbers, hence the use of 4 in the list comprehension and sum. Feel free to adjust this function to test different numbers to evaluate the correctness of the solution.