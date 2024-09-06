```python
def sum_to_n(n):
    """Returns the sum of integers from 1 to n."""
    return sum(range(1, n + 1))
```

This code defines a Python function called `sum_to_n` that takes a single argument, `n`, which is an integer representing the upper limit of a range of numbers. The function uses the `sum` function to calculate the sum of integers in the range from 1 to `n` (inclusive). The `range` function generates a sequence of numbers starting from 1 up to `n`, and the `sum` function adds up all the values in this sequence, providing the total sum of the integers from 1 to `n` as the result. 

This function is encapsulated in a Python script, which means it is self-contained and can be executed independently, providing a clean and organized way to manage code, and can be copied and pasted into a Python environment or script to solve the problem without any dependency. 

You can use the function by calling it with different values of `n` to calculate the sum of integers from 1 to `n` accordingly. 
For example:
```python
sum_to_n(30)  # The result should be 465
sum_to_n(100)  # The result should be 5050
sum_to_n(5)  # The result should be 15
sum_to_n(10)  # The result should be 55
sum_to_n(1)  # The result should be 1
```

This allows you to utilize the `sum_to_n` function to efficiently calculate the sum of numbers within a given range without the need for explicit looping constructs, making it a useful tool for various scenarios related to summation operations.