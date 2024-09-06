```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n+1)

def test_string_sequence(test_cases): 
    for i,case in enumerate(test_cases):
        assert case == str_sequence(int(case)),  
        print(f"Test passed for {i+1}")

test_string_sequence([0,5])
```

The above code defines a function `string_sequence` which returns a string containing space-separated numbers starting from 0 up to `n` (inclusive). The function uses the formula of `f` for `n`  to achieve this behavior, and the `test_string_sequence` function tests this `string_sequence` function with a series of test cases (0 and 5 in this case).  The `assert` statement is used to verify if the output of the `string_sequence` function matches the expected output for each input.