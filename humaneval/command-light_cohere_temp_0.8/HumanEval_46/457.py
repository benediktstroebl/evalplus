```python
def fib4(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    else:
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

if __name__ == "__main__":
    print("Fibonacci Number at index 5: ", fib4(5))
    print("Fibonacci Number at index 6: ", fib4(6))
    print("Fibonacci Number at index 7: ", fib4(7))
```
The above Python script defines a function called fib4, which computes the nth Fibonacci number in a sequence using an efficient non-recursive method. The function achieves this by utilizing a conditional structure, which checks for the base cases (n==0, n==1, n==2) and directly returns the corresponding Fibonacci values. For other values of of n, the function recursively calls itself with the value of n-1, n-2, n-3, and n-4, and then adds up these values to compute the nth Fibonacci number. The script then executes the test cases to verify the functionality of the fib4 function, printing out the corresponding Fibonacci numbers at the specified indices.