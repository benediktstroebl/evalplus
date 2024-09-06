```python
def sum_to_n(n):
    """Returns the sum of the first n integers.
    
    Args:
        n (int): Sum ends at nFh, inclusive. Must be a positive integer.
    
    Returns:
        int: The sum of integers from 1 to n.
    """
    # Calculate the sum
    sum_n = 0
    for num in range(1, n+1):
        sum_n += num
    return sum_n
```

This function uses a for loop to iterate through numbers from 1 to `n` (inclusive), and adds them to the variable sum_n. It returns `sum_n`, which represents the sum of the first `n` integers. This approach provides a clear and straightforward solution to the problem, following the intent of the provided documentation.

To ensure the function remains self-contained and adaptable to different scenarios, it includes an informative argument docstring, concise variable naming, and a descriptive function docstring. These elements collectively provide a clear understanding of the function's purpose, behavior, and expected inputs, making it convenient for utilization and further development. 

This approach allows the function to handle different input values and provides a reliable solution while maintaining a good grasp of the underlying concept.