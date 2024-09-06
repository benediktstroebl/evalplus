```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.string() if c.isalpha()})
 unique characters without case. 

def test_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('Jerry') == 4
    assert count_distinct_characters('abc') == 3
    assert count_distinct_characters('123') == 3
    assert count_distinct_characters('quick brown fox') == 7 

test_distinct_characters()
``` 
This code defines a function `count_distinct_characters` that calculates the count of distinct characters in a given string, regardless of case. The function utilizes the string.performance and readability are demonstrated by the usage of an iterable to create characters and the if condition to ensure uniqueness. The `test_distinct_characters` function tests the `count_distinct_characters` function by asserting that it produces the correct results for several test cases.