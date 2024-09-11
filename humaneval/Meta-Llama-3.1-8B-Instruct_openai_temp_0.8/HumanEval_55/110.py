### Fibonacci Number Calculator

Here's a simple Python script that uses dynamic programming to calculate Fibonacci numbers efficiently.

```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    The Fibonacci sequence is a series of numbers where a number is found by adding up the two numbers before it.
    Starting with 0 and 1, the sequence goes: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,...

    :param n: the position of the Fibonacci number to calculate
    :return: the n-th Fibonacci number
    """
    # Create a dictionary to store the Fibonacci numbers for memoization
    memo = {0: 0, 1: 1}

    # Calculate Fibonacci numbers from 2 to n
    for i in range(2, n + 1):
        # Calculate the i-th Fibonacci number as the sum of (i-1)-th and (i-2)-th numbers
        memo[i] = memo[i - 1] + memo[i - 2]

    # Return the n-th Fibonacci number
    return memo[n]


# Example usage:
if __name__ == "__main__":
    for n in range(1, 11):
        print(f"Fibonacci({n}) = {fib(n)}")
```

You can run this script to see the first 10 Fibonacci numbers printed out.

### Notes:

- The `fib` function uses a dictionary called `memo` to store previously calculated Fibonacci numbers. This technique is called memoization and significantly improves the performance of the function by avoiding redundant calculations.
- The function iterates from 2 to `n` (inclusive) to calculate each Fibonacci number, starting with the base cases 0 and 1.
- The final result is returned as the `n-th Fibonacci number`.