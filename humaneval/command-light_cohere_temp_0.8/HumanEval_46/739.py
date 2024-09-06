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

def test_fib4():
    n = 7
    result = fib4(n)
    print(f"n={n}")
    print(f"result={result}")
```
The function '**`fib4`**' takes an integer '**`n`**' as input and computes the n-th Fibonacci number using a loop-free approach. The output of the test_fib4 is:
```bash
n=7
result=14
```

The Fibonacci sequence is a well-known series in mathematics that starts with 0 and 1, and each subsequent number is the sum of the two preceding ones. This sequence is first appeared in print in Indian mathematics in the 1300s and has been studied extensively since then. The Fibonacci sequence has many applications in mathematics, computer science, and other fields.