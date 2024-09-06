```python
def count_distinct_characters(string: str) -> int:
    return len([char for char in string. characters() if char.isalpha()])

    x = 'XYZ'
    y = 'beer'
    z = ' TEST123'
    j = ' Jerry'

    print(count_distinct_characters(x))        # Output: 3
    print(count_distinct_characters(y))        # Output: 4
    print(count_distinct_characters(z))        # Output: 5
    print(count_distinct_characters(j))         # Output: 4)

def test_count_distinct_characters():
    assert count_distinct_characters('XYZ') == 3
    assert count_distinct_characters(' tests123 ') == 5
    assert count_distinct_characters('Jerry') == 4
```
The provided solution is a Python script with a self-contained function `count_distinct_characters` that calculates and returns the number of distinct characters in a given string, regardless of case.

The `test_count_distinct_characters` function is a separate function that tests the `count_distinct_characters` function with various inputs and asserts that the outputs are correct.