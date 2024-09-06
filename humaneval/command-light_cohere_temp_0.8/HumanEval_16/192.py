```python
def count_distinct_characters(string: str):
    return len(set(string))

#Tests
def test_count_distinct():
    assert count_distinct('xyzXYZ') == 3

def test_another_case():
    assert count_distinct('Jerry') == 4
``` 
This script provides a function `count_distinct_characters` that calculates the number of distinct characters in a given string, regardless of case. It uses a set data to collect and count these characters, and then returns the count. 

The test cases ensure that the function works as expected.