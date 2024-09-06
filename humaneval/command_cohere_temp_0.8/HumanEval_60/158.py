```python
def sum_to_n(n):
    """Returns the sum of the first n integers.

    Args:
        n (int): Number of integers to sum

    Returns:
        int: The sum of the first n integers
    """
    return sum(range(1, n + 1))
```

This code defines a function called `sum_to_n` that takes an integer argument `n`. It returns the sum of the first `n` integers from 1 to `n` inclusive. The code uses the `range` function to generate a sequence of numbers from 1 to `n` and then calls the `sum` function to add up all the numbers in the sequence. 

To verify the functionality of the code, execute the following tests cases in the console:
```python
>> sum_to_n(30)
465
>> sum_to_n(100)
5050
>> sum_to_n(5)
15
>> sum_to_n(10)
55
>> sum_to_n(1)
1
```

This should return the expected output for the test cases specified in the original problem.