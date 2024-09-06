```python
def string_sequence(n: int) -> str:
    return f"0 {n} {n+1} {n+2}"

# test case 1
assert string_sequence(0) == '0'

# test case 2
assert string_sequence(5) == '0 5 10 15 20'

# test case 3
try:
    assert string_sequence(10) == '0 10 19 26'
    except AssertionError as e:
        print(f"test case 10 failed with error: {e}")

# test case 4
try:
    assert string_sequence(1) == '0 1'
    except AssertionError as e:
        print(f"test case 1 failed with error: {e}")

# test case 5
try:
    assert string_sequence(15) == '0 15 10 25'
    except AssertionError as e:
        print(f"test case 15 failed with error: {e}")
```
The code defines a function called `string_sequence` that takes an integer `n` as input and returns a string containing space-delimited numbers starting from 0 and ending at `n+2`. The function uses an f-string format to construct the sequence.