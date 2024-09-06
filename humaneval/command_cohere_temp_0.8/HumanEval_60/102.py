```python
def sum_to_n(n):
    """Returns the sum of integers from 1 to n."""
    return sum(range(1, n + 1))
```

This code defines a Python function called `sum_to_n` that takes a single argument `n`, which is an integer. Inside the function, it uses the `sum` function in combination with the `range` function to calculate the sum of integers from 1 to `n`. The `range` function generates a sequence of numbers starting from 1 up to `n`, and the `sum` function adds up all the values in this sequence, giving you the total sum. This allows you to find the sum of numbers in a given range efficiently without manually counting or adding each number. 

The function documentation STRING 'Returns the sum of integers from 1 to n.' explains the purpose of the function. Overall, this code provides a simple and efficient way to calculate the sum of integers within a specified range, making it a useful tool for various numeric applications. 

You can use this function to calculate the sum of numbers from 1 to any desired value `n` by passing it as an argument, such as `sum_to_n(10)` to find the sum of numbers up to 10.