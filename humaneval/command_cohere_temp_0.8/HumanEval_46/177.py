```python
def fib4(n):
    fib4_list = [0, 0, 2, 0]
    for i in range(5, n+1):
        fib4_list.append(fib4_list[i-1] + fib4_list[i-2] + fib4_list[i-3] + fib4_list[i-4])
    return fib4_list[n]
```

This script defines the `fib4()` function, which efficiently calculates the n-th element of the Fib4 sequence without using recursion. It initializes a base list (`fib4_list`) with the first five elements of the sequence and then iteratively computes subsequent elements by summing the last four elements in the list, updating the list accordingly. Finally, it returns the n-th element from the updated list. 

This approach is optimized and avoids the exponential time complexity issues associated with recursive solutions. It utilizes a steady progression of constant time operations, making it efficient for larger values of `n`.