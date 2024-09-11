```python
def mem_fibfib(n: int, memo: dict = {}):
    """
    This function calculates the nth element of the FibFib number sequence.
    
    Args:
        n (int): The position of the element to be calculated.
        memo (dict): A dictionary to store the results of subproblems (default is {}).
    
    Returns:
        int: The nth element of the FibFib number sequence.
    """
    
    # Base cases
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    
    # Create memo if it doesn't exist
    if not memo:
        memo = {0: 0, 1: 0, 2: 1}
    
    # If the result is already in the memo, return it
    if n in memo:
        return memo[n]
    
    # If not, calculate the result and store it in the memo
    result = mem_fibfib(n-1, memo) + mem_fibfib(n-2, memo) + mem_fibfib(n-3, memo)
    memo[n] = result
    
    return result

# Test the function
print(mem_fibfib(1))  # Output: 0
print(mem_fibfib(5))  # Output: 4
print(mem_fibfib(8))  # Output: 24
```

This script uses memoization to store the results of subproblems, which makes it efficient by avoiding redundant calculations. The base cases are handled first, and then the function calculates the result for the given `n` and stores it in the `memo` dictionary. If the result is already in the `memo`, it simply returns the stored value.