```python
def fib4(n: int) -> int:
    fib4_numbers = [0, 0, 2, 0]
    for i in range(5, n + 1):
        fib4_numbers.append(fib4_numbers[i - 1] + fib4_numbers[i - 2] + fib4_numbers[i - 3] + fib4_numbers[i - 4])
    return fib4_numbers[n]
```

This script defines the `fib4` function, which efficiently calculates the n-th element of the Fib4 sequence, as described in the problem statement. It initializes a list (`fib4_numbers`) with the first 5 elements of the sequence and then iteratively computes subsequent elements by summing the values from the last four elements in the list. Finally, it returns the n-th value from the list, ensuring each value is computed only once. This approach avoids repeated calculations and improves performance, making it an efficient solution.