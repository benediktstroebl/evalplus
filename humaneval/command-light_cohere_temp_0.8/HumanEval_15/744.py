Here is a self-contained Python script that solves the problem you described:

```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive """
    return f"0 {n}:{n+1}" * (n+1)

# Test cases
test_sequence = [
    (0, "0"),
    (1, "1"),
    (5, "0 5 6 7 8 9"),
    (100, "0 100 101 102 103 104 105 106")
]

for n, expect in test_sequence:
    actual = string_sequence(n)
    print(f"Test {n}: {actual} == {expect}")
```
The code defines a function `string_sequence` that generates a sequence of numbers in the form of a string, starting from 0 and ending at the number n, and then prints the result. The test cases are also passed to the `string_sequence` function with different values of `n` and are then printed to the console.