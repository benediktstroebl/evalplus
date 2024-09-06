```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string. string()})
return len(set(string))

# Test suite
def test():
    assert count_distinct_characters('abc') == 3
    assert count_distinct_characters('ABC') == 3
    assert count_distinct_characters('abcABC') == 3
    assert count_distinct_characters('XyX') == 3
    assert count_distinct_characters('yXx') == 2
    assert count_distinct_characters('jj') == 2
    assert count_distinct_characters('jerry') == 4

if __name__ == "__main__":
    test()
```
This script defines a function `count_distinct_characters` that calculates the count of unique characters in a given string. The function utilizes the simple list comprehension and set membership checks to achieve this. The `test` function is also provided to run and validate the correctness of this function with various inputs.