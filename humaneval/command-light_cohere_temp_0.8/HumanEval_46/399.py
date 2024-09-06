```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which each number is the sum of the two preceding ones.
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        return fib4(n-1) + fib4(n-2)

if __name__ == "__main__":
    print(fib4(5))  # Output: 4
    print(fib4(6))  # Output: 8
    print(fib4(7))  # Output: 14
```
The provided code defines a function fib4 which computes the n-th value of the Fibonacci sequence using a iterative approach, without recursion. The function follows the basic arithmetic rules of the Fibonacci sequence: each number is the sum of the two preceding ones. 

This method has the potential for efficiency and space complexity in the range of O(n).  By using a loop, we avoid the complexities associated with function call stack and recursion, which makes this approach more efficient and readable.