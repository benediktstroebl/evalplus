```python
def sum_to_n(n):
    """Returns the sum of the first n integers.

    Args:
        n (int): Number of integers to sum.

    Returns:
        int: The sum of the first n integers.
    """
    return sum(range(1, n + 1))
```
This Python script defines a function called sum_to_n, which takes an integer argument n and returns the sum of the first n integers. The function uses the sum function to calculate the sum of the range from 1 to n, inclusive.

To use this function, you can call it with a specific value of n and assign the result to a variable, like this:
```python
result = sum_to_n(10)
print(result)  # Output: 55
```
This will print the sum of the first 10 integers, which is 55, as demonstrated in the test cases provided earlier. Feel free to test the function with different values of n to observe the corresponding results. This function provides a convenient way to calculate the sum of numbers within a specific range, making it useful for various applications that involve quantitative analysis and summation operations.