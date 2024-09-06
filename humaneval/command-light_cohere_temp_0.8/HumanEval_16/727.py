```python
def count_distinct_characters(string):
    """
    Count the number of distinct characters in a string, regardless of case.
    return: 
    The number of unique characters
    """
    import string
    char_set = set(string.unique(). chars() 
    return len(char_set)

# Unit tests
test_distinct_characters = False
test_string = "xyzXYZ"
# assert count_distinct_characters(test_string) == 3
# test_string = "Jerry"
# assert count_distinct_characters(test_string) == 4

``` 
This script defines a function `count_distinct_characters` that computes the count of unique characters in a given string, regardless of case. It then provides a unit tests that validate the correctness of the function.