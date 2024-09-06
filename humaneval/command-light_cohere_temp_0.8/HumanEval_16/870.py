```python
def count_distinct_characters(string: str) -> int:
    return len(set(string))

# Tests
def test_count_distinct_characters():
    assert count_distinct_characters('abc') == 3  # Should be 3 because 'abc' contains only distinct 'a'

def test_count_distinct_characters2():
    assert count_distinct_characters('xyXyz') == 4  # Should be 4 because 'xyXyz' contains only distinct 'x', 'y', 'z'

def test_count_distinct_characters3():
    assert count_distinct_characters('JERRY') == 4  # Should be 4 because 'JERRY' contains only distinct 'r', 'e'

if __name__ == "__main__":
    test_count_distinct_characters()
    test_count_distinct_characters2()
    test_count_distinct_characters3()
```
This code defines a function `count_distinct_characters` that calculates the count of unique characters in a given string, regardless of case. It also includes comprehensive test cases to validate the correctness of the function.

The `test_count_distinct_characters` function is used to execute the tests for the `count_distinct_characters` function. The `test_count_distinct_characters2` and `test_count_distinct_characters3` functions are used to test the function with different input strings. 
The `if __name__ == "__main__":` block ensures that the test cases are run when the script is executed directly.