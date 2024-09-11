```python
def fibfib(n: int) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    
    Args:
        n (int): The position of the element in the sequence.
    
    Returns:
        int: The n-th element of the FibFib number sequence.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    elif n < 3:
        raise ValueError("Input should be an integer greater than 2")
    else:
        # Initialize a list to store the previously calculated values
        fibfib_sequence = [0, 0, 1]
        
        for i in range(3, n+1):
            # Calculate the next value using the formula: fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
            next_value = fibfib_sequence[i-1] + fibfib_sequence[i-2] + fibfib_sequence[i-3]
            # Append the calculated value to the list
            fibfib_sequence.append(next_value)
        
        # Return the n-th element of the sequence
        return fibfib_sequence[n]

# Test cases
print(fibfib(1))   # Output: 0
print(fibfib(5))   # Output: 4
print(fibfib(8))   # Output: 24
```

However, the function above has a time complexity of O(n) due to the repeated computation of the same intermediate values. To improve the efficiency, we can use dynamic programming with a technique called memoization to store the previously calculated values.

Here's an optimized version of the function with a time complexity of O(n):

```python
def fibfib(n: int) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    
    Args:
        n (int): The position of the element in the sequence.
    
    Returns:
        int: The n-th element of the FibFib number sequence.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    elif n < 3:
        raise ValueError("Input should be an integer greater than 2")
    else:
        # Initialize a dictionary to store the previously calculated values
        memo = {0: 0, 1: 0, 2: 1}
        
        def fibfib_recursive(i: int) -> int:
            if i not in memo:
                # Calculate the next value using the formula: fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
                memo[i] = fibfib_recursive(i-1) + fibfib_recursive(i-2) + fibfib_recursive(i-3)
            return memo[i]
        
        # Return the n-th element of the sequence
        return fibfib