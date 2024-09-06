```python
def fib4(n):
    fib4_list = [0, 0, 2, 0]
    for i in range(5, n + 1):
        fib4_list.append(fib4_list[i - 1] + fib4_list[i - 2] + fib4_list[i - 3] + fib4_list[i - 4])
    return fib4_list[n]
```
This code defines a function `fib4` which efficiently calculates the n-th number in the Fib4 sequence, based on the definition of the sequence. The function starts with the first 5 numbers in the sequence (up to 3rd paranthesis in the sequence definition) and iteratively calculates subsequent numbers up to the n-th number, using a loop. The result is the value of the n-th number in the Fib4 sequence.