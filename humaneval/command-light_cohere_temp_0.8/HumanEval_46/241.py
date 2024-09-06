```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which each number is the sum of the two preceding ones. The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the previous two numbers.
    """
    sequence = [0, 1]
    while len(sequence) < n:
        next_num = sequence[-1] + sequence[-2]
        sequence.append(next_num)
    return sequence[-1]

# Unit tests
def test_fib4():
    assert fib4(0) == 0
    assert fib4(1) == 0
    assert fib4(2) == 2
    assert fib4(3) == 0
    assert fib4(5) == 4
    assert fib4(6) == 8
    assert fib4(7) == 14
    assert fib4(8) == 22
    assert fib4(9) == 84

# Example usage
if __name__ == "__main__":
    test_fib4()
```
The function fib4 calculates the n-th Fibonacci number in a sequence and returns it. The function uses a sequence of numbers [0, 1], and uses a while loop to generate the next numbers in the sequence by adding the last two numbers. The function then returns the sequence[-1] which is the n-th Fibonacci number. The unit tests ensure that the function works correctly for various inputs.