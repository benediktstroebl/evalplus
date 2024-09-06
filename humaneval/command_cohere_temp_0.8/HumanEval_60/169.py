```python
def sum_to_n(n):
    """Returns the sum of integers from 1 to n."""
    return sum(range(1, n + 1))
```
This Python script defines a function called sum_to_n, which takes an input n, representing the upper limit of a range of numbers. The function utilizes the sum function to calculate the sum of integers ranging from 1 to n. This is achieved by using the range function to generate a sequence of numbers from 1 to n, including both endpoints, and passing this sequence to the sum function for addition. The result of this calculation is the total sum of all integers between 1 and n. This provides a convenient way to obtain the cumulative value of a range of numbers without manually summing each term.