```python
def fib4(n: int):
    if n <= 0:
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
    assert fib4(5) == 4
    assert fib4(6) == 8
    assert fib4(7) == 14

def main():
    test_fib4()

if __name__ == "__main__":
    main()
``` 
The function `fib4` uses a bottom-up approach to calculate the n-th Fibonacci number in the Fibonacci sequence. It begins with a base cases for n=0, 1, and 2, and then continues to calculate the next terms in the sequence by summing the preceding three terms. 
The test_fib4 function tests the function by calling it with various values of n and asserting that the results are correct. 
The code is self-contained and does not rely on any external functions or modules, making it easy to understand and maintain.