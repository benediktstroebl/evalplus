Here's a Python script that contains a function called `get_odd_collatz` that solves the problem in a markdown code block:
```python
def get_odd_collatz(n):
    odd_collatz = []
    sequence = [n]
    while len(sequence) > 0:
        current = sequence.pop()
        if current % 2 == 0:
            sequence.append(current / 2)
        else:
            sequence.append(3 * current + 1)
        if current % 2 != 0:
            odd_collatz.append(current)
    odd_collatz.sort()
    return odd_collatz
```

This script defines a function called `get_odd_collatz` that takes in a positive integer `n` as input and returns a sorted list of odd numbers in the Collatz sequence. The function starts with the given number `n` and iteratively applies the Collatz sequence rules (dividing by 2 if even, else multiplying by 3 and adding 1 if odd) to generate the sequence. It keeps track of odd numbers in the `odd_collatz` list, which is eventually returned after sorting it in ascending order.

Here is a simple test to validate the functionality of the code:
```python
def test_get_odd_collatz():
    assert get_odd_collatz(1) == [1]
    assert get_odd_collatz(5) == [1, 5]
    assert get_odd_collatz(10) == [1, 5, 10]

test_get_odd_collatz()
```

This test verifies that the function behaves as expected for three different inputs: `1`, `5`, and `10`.  This is a good start, but remember that the Collatz sequence can grow very rapidly, so the true correctness of this function is ultimately tied to the validity of the Collatz conjecture!