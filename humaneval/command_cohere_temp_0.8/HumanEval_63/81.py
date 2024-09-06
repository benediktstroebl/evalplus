```python
from collections import defaultdict

def fibfib_n(n: int):
    if n < 0:
        raise ValueError("FibFib is only defined for non-negative integers.")
    
    mod = 10**9 + 7 
    fibfib = defaultdict(int)
    fibfib[0] = 0
    fibfib[1] = 0

    for i in range(2, n + 1):
        fibfib[i] = (fibfib[i-1] + fibfib[i-2] + fibfib[i-3]) % mod

    return fibfib[n]

def main():
    import doctest
    doctest.testmod(verbose=1)

if __name__ == "__main__":
    main()
```

This code defines a function `fibfib_n` that computes the n-th FibFib number efficiently. It initializes the FibFib numbers up to the (n-1)th position and uses a dictionary to store these numbers while updating them dynamically based on the definition of the FibFib sequence, ultimately computing the n-th FibFib number.

The `main` function calls the `doctest.testmod` function to verify the correctness of the `fibfib_n` function by checking its behavior against the example uses provided in the docstring. The verbose=1 argument ensures that detailed test results are displayed, making it easier to identify any issues or errors in the code.

The `if __name__ == "__main__":` block is a common Python idiom that ensures the `main` function is executed only when the script is run directly, not when it's imported as a module. This way, the code structure is more organized and testable, as described in the Python Pitfalls book.