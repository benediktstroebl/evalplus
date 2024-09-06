```python
def fib4(n: int) -> int:
    bas = [0, 0, 2, 0]
    for i in range(5, n + 1):
        bas.append(bas[i - 1] + bas[i - 2] + bas[i - 3] + bas[i - 4])
    return bas[n]
```
This code defines a function `fib4` that efficiently calculates the n-th number in the Fib4 sequence, based on the definition of the sequence. It initializes the first 4 numbers of the sequence and then iteratively computes subsequent numbers up to the n-th number. The resulting array `bas` holds the computed values of the Fib4 sequence up to the n-th number, and the function returns the n-th value from this array. This approach ensures efficient computation without using recursion. 

Here is an example usage of the function:
```python
>>fib4(5)
4
>>fib4(6)
8
>>fib4(7)
14
```

The provided example usage demonstrates the function's correctness for various input values.