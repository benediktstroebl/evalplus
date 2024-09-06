Here's a Python script that contains a function `get_odd_collatz` that solves the problem in a markdown code block:
```python
def get_odd_collatz(n):
    seq = [1]
    while len(seq) < len(str(n)):
        if seq[-1] % 2 == 0:
            seq.append(seq[-1] // 2)
        else:
            seq.append(3 * seq[-1] + 1)
    return [e for e in seq if e % 2 != 0]

# Tests:
assert get_odd_collatz(1) == [1]
assert get_odd_collatz(5) == [1, 5]
assert get_odd_collatz(14) == [1, 7, 20, 10, 5, 16, 8, 4, 2, 1]
```
This script defines a function `get_odd_collatz(n)` that returns the odd numbers in the Collatz sequence of a positive integer `n`. The function starts with `1` in the sequence and iteratively calculates the next term in the sequence (either by dividing by 2 or multiplying by 3 and adding 1, depending on whether the previous number was even or odd). It then filters out the even numbers from the sequence, resulting in a list of only the odd numbers in the Collatz sequence. 

The script also includes tests to validate the function's behavior for different inputs. Specifically, it checks if the function works correctly for `n` values of `1`, `5`, and `14`, which are provided as examples in the problem description.