```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which the second element is the sum of the first two elements, and each subsequent element is the sum of the previous two elements.
    """
    previous_sum = 0
    current_sum = 0
    for _ in range(n):
        current_sum += previous_sum
        previous_sum = current_sum
    return current_sum

# Example usage
test_fib4 = fib4(7)
print("The Fibonacci number at position 7 is:", test_fib4)
```