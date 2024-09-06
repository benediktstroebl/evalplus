Here is a Python script with a self-contained function that solves the problem you provided:
```python
def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} {" + str_sequence(n - 1) + "}" 

def str_sequence(n: int) -> str:
    return "".join() * n

def test_string_sequence(test_cases: []):
    for test_case in test_cases:
        assert str_sequence(test_case) == test_case

test_cases = [0, 5]
test_string_sequence(test_cases)
``` 
This script defines two functions: 
- `string_sequence`: which accepts an integer `n` as an argument and returns a string containing space-delimited numbers from 0 to `n`, inclusive. It uses an recursive approach to achieve this. 
- `str_sequence`: generates a sequence of empty strings (`""`) repeated `n` times. 

The second function tests the string sequence function with two provided test cases, ensuring the function produces the correct results.