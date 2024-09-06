```python
def sum_to_n(n):
    """Returns the sum of the first n integers.
    >>> sum_to_n(30)
    465
    >>> sum_to_n(100)
    5050
    >>> sum_to_n(5)
    15
    >>> sum_to_n(10)
    55
    >>> sum_to_n(1)
    1
    """
    return sum(range(1, n + 1))
```
The code defines a function `sum_to_n` taking a single argument `n` which returns the sum of the first `n` integers. It uses the generator expression `range(1, n+1)` to produce the sequence of numbers from 1 to `n` and the built-in `sum` function to add them all together. The `sum` function adds the numbers together element-wise to produce the total sum. 

This approach provides an efficient solution to the problem without exceeding the memory requirements of the motherboard, as it only generates the integers from 1 to `n` one at a time. 

The docstring of the function provides several test cases to verify its correctness. These test cases can be executed by adding the `>>>` prompt in the Python interpreter, followed by pasting the test cases inside the parentheses and finally pressing Enter to execute them. 

You can use this code in your own Python projects, and it can be adapted and modified to suit other scenarios involving sequential sum calculations. 
If you have any questions or need further assistance, feel free to ask!