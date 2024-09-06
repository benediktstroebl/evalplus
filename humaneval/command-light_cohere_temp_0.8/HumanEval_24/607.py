Here is a Python script with a self-contained function that finds the largest divisor of a given number:
```python
import math
def largest_divisor(n: int) -> int:
    # Initialize the largest divisor found so far
    dp = [0] * (math.max + 1)
    larger divisor possible for n in range(1, math.5 + 1)
   
    # Initialize the largest divisor as 1
    for i in range(2, math.5 + 1):
        dp[i] = i
    # Search through all numbers smaller than n
    for j in range(n, 1, -1):
        # Check if j divides n
        if j == int(n / j):
            # Update the largest divisor if greater or equal to the current largest divisor
            if dp[j] <= i:
                dp[j] = i
    return dp[1]  # Return the largest divisor found
```