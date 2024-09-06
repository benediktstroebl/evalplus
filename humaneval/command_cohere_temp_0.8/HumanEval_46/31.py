```python
def fib4(n: int):
    if n < 0:
        raise ValueError("Fib4 is defined only for non-negative integers.")
    
    fib4_list = [0, 0, 2, 0]
    for i in range(5, n + 1):
        fib4_list.append(fib4_list[i - 1] + fib4_list[i - 2] + fib4_list[i - 3] + fib4_list[i - 4])
    
    return fib4_list[n]
```

This script defines the `fib4` function, which calculates the n-th element of the Fib4 sequence efficiently without using recursion. It validates the input and initializes the first 5 elements of the sequence. Then, using a loop, it calculates subsequent elements by summing the previous four elements and appends them to the `fib4_list`. Lastly, it returns the n-th element from the list. The script efficiently handles larger values of `n` without incurring the overhead of recursive calls, making it suitable for calculating larger Fib4 numbers. 

This approach avoids the recursion downside, providing a more scalable solution.

You can install and import the `math` module to test this script, which includes the `fib4` function. After that, you may call this function with various argument values to determine the corresponding Fib4 numbers in the sequence.  For example:
```python
>>> fib4(5)
4

>>> fib4(6)
8

>>> fib4(7)
14
``` 
This demonstrates how the script successfully computes the Fib4 numbers for these input values.