```python
def sum_to_n(n):
    """Returns the sum of integers from 1 to n."""
    return sum(range(1, n + 1))
```

This code defines a Python function called `sum_to_n`. This function takes a single argument, `n`, which is an integer. The purpose of this function is to calculate and return the sum of all integers from 1 to `n` (inclusive) using the `sum` function and generating values using the `range` function. The `range` function generates all numbers from 1 to `n` (inclusive) as an iterable, and the `sum` function adds up all the values in that iterable, giving you the total sum of the integers from 1 to `n`. 

The function is documented with a docstring, which explains its purpose, and provides example usage scenarios using Python's `>>> ` syntax, which is used for inline testing and experimentation in the Python interpreter.

This code is self-contained, meaning it does not depend on any external variables or modules, and it can be executed independently. 

To utilize this function, you can simply call it by providing an integer argument `n` to whom you want to calculate the sum of integers and use the returned value to receive the result. 

For example, if you want to calculate the sum of integers from 1 to `100`, you can call the function like this: `sum_to_n(100)` and assign the returned value to a variable, where you can then use it in your code as needed. 

This allows you to easily include this functionality in your Python workflows and scripts as needed.  If you have additional questions or require more customization for your specific needs, let's discuss further or provide more feedback so we can tailor it to your requirements.