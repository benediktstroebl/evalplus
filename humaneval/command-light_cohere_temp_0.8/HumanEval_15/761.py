```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n+1)

# Test case 1: Check if function returns the right sequence of numbers
def test_case_1(test_num: int) -> None:
    assert string_sequence(test_num) == f"0 {test_num}"* (test_num+1)
    return

# Test case 2: Check if function handles negative input
def test_case_2(test_num: int) -> None:
    string_sequence(-test_num)
    assert True

# Test case 3: Check if function handles large values of n
def test_case_3(test_num: int) -> None:
    assert string_sequence(test_num) == f"0 {test_num}"* (test_num+1)
    return
```