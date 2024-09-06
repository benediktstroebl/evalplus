```python
def choose_num(x, y):
    max_even = -1
    i = x
    while i <= y:
        if i % 2 == 0:
            max_even = i
        i += 1
    return max_even
```

The function `choose_num()` takes two parameters, `x` and `y`, and searches for the biggest even integer that exists in the range `[x, y]` (inclusive). It does so by initializing `max_even` to -1 and then iterating through the range with a while loop, checking if each integer is even, and updating `max_even` if so. The loop exits when `i` reaches `y`, and the function returns the maximum even number found, or -1 if no even number is found in the range. 

Here is a simple test suite for that code:
```python
def test_choose_num():
    # Basic Test Cases
    assert choose_num(12, 15) == 14
    assert choose_num(13, 12) == -1
    assert choose_num(2, 10) == 8
    
    # Edge Cases
    assert choose_num(1, 10) == -1
    assert choose_num(10, 20) == 10
    assert choose_num(0, 100) == -1
    
    # Cases with No Even Number
    assert choose_num(3, 5) == -1
    assert choose_num(7, 11) == -1
``` 

To test the function, a test suite with various scenarios is recommended to ensure that the function behaves as expected and aligns with the problem statement. You can add more tests depending on specific scenarios you'd like to cover. 

The `test_choose_num()` function utilizes the `choose_num()` function from the codebase and asserts that the returned values are as expected for various inputs. 

You can run this test suite by adding the above code to a Python file (e.g., `test_choose_num.py`) and then running `python test_choose_num.py` in your terminal.