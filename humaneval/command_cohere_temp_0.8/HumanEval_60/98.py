```python
def sum_to_n(n):
    """Returns the sum of the first n integers.
    Args:
        n (int): Number of integers to sum up to.
    Returns:
        int: The sum of the first n integers.
    """
    return sum(range(1, n + 1))
```

This code defines a function called sum_to_n, which takes an integer n as input and returns the sum of the first n integers. The function uses the range function to generate a sequence of numbers from 1 to n, and the sum function to add up all the numbers in the sequence. 

The function is designed to be efficient and uses two built-in Python functions, range, and sum, to perform its task. The resulting sum is computed without keeping track of previously calculated sums and thus has a linear time complexity of O(n). 

The function accepts an integer argument n, which specifies the number of integers to be included in the sum. The function returns the sum of the first n integers, starting from 1 up to and including n. 

This Python script solves the problem in a self-contained manner, and the function sum_to_n can be reused in other projects to efficiently calculate the sum of integers within a specified range.