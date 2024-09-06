```python
def string_sequence(n: int) -> str:
    if n < 0:
        raise ValueError("n should be positive")
    if n == 0:
        return '0'
    sequence = [i for i in range(1, n+1)]
    return ' '.join(sequence)

#test cases
test_seq = string_sequence(0)
assert test_seq == '0'
test_seq = string_sequence(5)
assert test_seq == '0 1 2 3 4 5'
test_seq = string_sequence(-5)
assert test_seq == '0'
test_seq = string_sequence(10)
assert test_seq == '0 9 8 7 6 5 4 3 2 1'
```
This code defines a function called `string_sequence` that generates a string containing space-separated numbers from 0 up to a given positive integer n. The function handles the basic input validation to ensure that n is positive, and then constructs and returns a string containing the sequence of numbers from 0 up to n. Finally, there are several test cases provided to check the correctness of the `string_sequence` function.