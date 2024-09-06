```python
def count_distinct_characters(string: str):
    return len([char for char in string.str.case.isalpha()])
 whole function

def test_distinct_characters():
    assert count_distinct_characters('abc') == 3
    assert count_distinct_characters('XYZ') == 3
    assert count_distinct_characters(' Jerry') == 4

``` 
This code defines a function `count_distinct_characters` that calculates the number of unique characters in a given string, regardless of case. The function uses the array comprehension and the `islower` function to achieve this. The `test_distinct_characters` function tests the `count_distinct_characters` function with various input strings.