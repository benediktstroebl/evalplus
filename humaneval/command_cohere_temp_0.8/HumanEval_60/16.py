```python
def sum_to_n(n):
    """Returns the sum of integers from 1 to n."""
    return sum(range(1, n + 1))
```

This code defines a Python function called `sum_to_n`. This function takes a single argument, `n`, which is an integer. The purpose of this function is to calculate and return the sum of all integers from 1 to `n` (inclusive). It uses the `sum` function to add up all the values in the `range` of numbers from 1 to `n`, including both 1 and `n`. To use this function, you can call it with a value for `n`, and it will return the sum of integers from 1 to that `n`. 

Here is an example of how you might call this function with different values for `n`:
```python
sum_to_n(5)  # This will return 15, the sum of integers from 1 to 5
sum_to_n(10)  # This will return 55, the sum of integers from 1 to 10
sum_to_n(30)  # This will return 465, the sum of integers from 1 to 30
``` 
```
sum_to_n(1)  # This will return 1, the sum of integers from 1 to 1 (i.e., 1 + 1 = 2)
```
Note that the sum of integers from 1 to 1 is technically 2, not 1, because the range includes both 1 and 2.

Also, this Markdown code block includes a docstring, which is a multi-line comment enclosed in triple quotes. These strings provide detailed information about the function, serving as a form of documentation. The docstring describes the purpose of the `sum_to_n` function, and provides examples of its usage alongside expected output. These docstrings are a great way to explain how to use a function and what value it provides, making your code more accessible to others (and to your future self).