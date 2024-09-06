```python
def count_distinct_characters(string):
    """
    Count the number of distinct characters in a given string, ignoring case.
    return:
    total_distinct_characters
    """
    import string
    char_set = set(string.nlower())
   
    distinct_chars = len(char_set)
    return distinct_chars

# Test cases
assert count_distinct_characters('xyzXYZ') == 3
assert count_distinct_characters('jerry') == 4
assert count_distinct_characters(' ') == 0
assert count_distinct_characters('   '') == 0

```
This Python code defines a function called `count_distinct_characters`, which aims to determine the total count of unique characters in a given string, irrespective of case. The function utilizes the input as a string and employs the `set` data structure to create a character set, ensuring all characters are unique. The `set` method automatically removes duplicate characters, and its length represents the total count of distinct characters. This function then returns this result, which is the count of distinct characters found in the input string.

Note: This code is optimized for efficiency, and it's a good starting point for solving the problem. However, depending on the specific requirements or constraints of your use case, further improvements might be necessary.