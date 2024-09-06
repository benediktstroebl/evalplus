Here's a Python script with a self-contained function `get_odd_collatz` that solves the problem:
```python
def get_odd_collatz(n):
    odd_seq = [3*i+1 for i in range(1, n//2 + 1)] if n % 2 else [1]
    even_seq = [x//2 for x in range(n, 1, -1)]
    return odd_seq + [x for x in even_seq if x % 2 == 1]

# Tests:
assert get_odd_collatz(1) == [1]
assert get_odd_collatz(5) == [1, 5]
assert get_odd_collatz(14) == [1, 7, 20, 10, 5, 16, 8, 4, 2, 1]
```
This approach first determines whether N is odd. If it is, create a list with the first odd number (3i + 1). If N is even, create a list with a single element, 1. Then, in either case, we create a list of even numbers by dividing N by 2 until it reaches 1. Then, in the result, we only add the odd numbers by filtering the even sequence.