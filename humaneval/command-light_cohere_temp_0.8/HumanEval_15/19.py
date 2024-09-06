```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} 000" * (n + 1)

#Test cases
test_seq = []
for i in range(10):
    test_seq.append(f"{i}:>n}".format(n=i)

def test_function_seq(test_case: str) -> None:
    assert test_seq == test_case, f"Should be {test_case} but got {test_seq}"
    return

#Test cases
test_function_seq(test_seq)
```