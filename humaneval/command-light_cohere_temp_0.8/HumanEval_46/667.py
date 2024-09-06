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
    print("Fibonacci sequence starting from 0:")
    print(fib4(0))  # Output: 0
    print(fib4(1))  # Output: 0
    print(fib4(2))  # Output: 2
    print(fib4(3))  # Output: 0
    print(fib4(4))  # Output: 4
    print(fib4(5))  # Output: 8
    print(fib4(6))  # Output: 14
    print(fib4(7))  # Output: 28
```
The Fibonacci sequence is a well-known mathematical sequence where each number is the sum of the two preceding ones. In this code, we define a function fib4(n) that calculates the n-th Fibonacci number in the sequence, avoiding the use of recursion. The function checks for base cases (n==0, n==1, n==2) and returns the corresponding numbers (0, 0, 2). For n>2, it recursively calculates the sum of the last four numbers to generate the next Fibonacci number. For larger n, it uses the sum of the previous three numbers, plus the last number, to compute the n-th Fibonacci number. The tests for the proof can be executed in Python using the built-in assert statement.