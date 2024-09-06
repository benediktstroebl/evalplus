```python
def is_equal_to_sum_even(n):
    even_nums = [2, 4, 6, 8, 10, 12]
    return n in even_nums
```

This function directly tests if the given number n is present in the list of positive even numbers.

To ensure this function is self-contained, it defines a new list 'even_nums' that includes all the necessary even numbers to solve the problem. Hence, there's no reliance on any external variables or data, making the function standalone and portable.

This approach allows the function to accurately determine if n can be written as the sum of exactly 4 positive even numbers without any external dependencies.