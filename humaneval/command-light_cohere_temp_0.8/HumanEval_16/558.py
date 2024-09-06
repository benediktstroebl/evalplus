```python
def count_distinct_characters(string: str) -> int:
    return len(set(string))

def test_count_distinct_characters():
    assert count_distinct_characters('abc') == 3
assert count_distinct_characters('ABC') == 3
assert count_distinct_characters(' Zoo ) == 5
assert count_distinct_characters('hello123 ') == 8

``` 
This code defines a function `count_distinct_characters` that computes the number of distinct characters in a given string, regardless of case. The `test_count_distinct_characters` function contains assertions that test the correctness of this function with various input strings.  This expected output is 3 distinct characters for the string 'abc'.