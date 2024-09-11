### FibFib Number Sequence Calculator

Below is a Python script that efficiently calculates the n-th element of the FibFib number sequence using memoization.

```markdown
### Code
```python
def fibfib(n: int, memo: dict = {}):
    """
    The FibFib number sequence is a sequence similar to the Fibbonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).

    Args:
    n (int): The index of the FibFib number to calculate.
    memo (dict): A dictionary to store previously calculated values.

    Returns:
    int: The n-th element of the FibFib number sequence.
    """
    if n in memo:
        # If the value is already in the memo, return it
        return memo[n]
    
    # Base cases
    if n == 0 or n == 1:
        result = 0
    elif n == 2:
        result = 1
    else:
        # Recursive case
        result = fibfib(n-1, memo) + fibfib(n-2, memo) + fibfib(n-3, memo)
    
    # Store the result in the memo
    memo[n] = result
    
    return result


# Test cases
print(fibfib(1))  # 0
print(fibfib(5))  # 4
print(fibfib(8))  # 24
```

### Explanation

This script defines a function `fibfib` that calculates the n-th element of the FibFib number sequence. It uses a dictionary `memo` to store previously calculated values, which helps to avoid redundant calculations and improves efficiency.

The function checks if the value is already in the `memo` dictionary before calculating it. If it is, the function returns the stored value. Otherwise, it calculates the value recursively and stores it in the `memo` dictionary.

The base cases are handled directly, and the recursive case is calculated using the `memo` dictionary. The result is then stored in the `memo` dictionary to avoid redundant calculations in the future.

The test cases demonstrate the correctness of the function.