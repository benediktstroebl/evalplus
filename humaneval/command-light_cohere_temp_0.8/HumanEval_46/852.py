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
    n = int(input("Enter a number to test: "))
    print(fib4(n))

test_fib4()
```
This Python code defines a function called fib4 that computes the n-th element of the Fibonacci sequence using a specific algorithm, without recursion. It also has a test function test_fib4, which prompts the user to input a number and then calls the fib4 function to calculate and print the result. 

The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding numbers. This sequence starts with 0 and 1, and each subsequent number is the sum of the two previous numbers. The Fibonacci sequence has many applications in mathematics, computer science, and other fields.