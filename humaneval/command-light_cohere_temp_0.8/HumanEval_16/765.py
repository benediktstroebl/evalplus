Here is a Python script that contains a self-contained function to solve the problem of counting the number of distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.string() if c.isalpha()})
 unique characters 
def test_count_distinct_characters(test_string): 
    assert count_distinct_characters(test_string) == len(set(test_string)) 

#test_string = "xyzXYZ jerry jEff" 

test_count_distinct_characters(test_string)

``` 
This script defines a function `count_distinct_characters` that calculates the number of distinct characters in a given string, and a related test function `test_count_distinct_characters` that ensures the function's correctness when provided with a test string.  The script then defines a test string and passes it to `test_count_distinct_characters` function to test its functionality.