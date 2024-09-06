```python
def count_distinct_characters(string: str):
    return len([char for char in string.i if char not in 'abcdefghijklmnopqr'])

# Test cases
test_count_distinct_characters = """
def test_count_distinct_chars():
    assert count_distinct_characters('abc') == 3
assert count_distinct_characters('XYabc') == 3
assert count_distinct_characters('hello world') == 6
assert count_distinct_characters('1234') == 4
assert count_distinct_characters(' ' ) == 0
def main():
    test_count_distinct_chars()
main()
"""
# Run the main function
# Perform the tests when you run the script
``` 
This script defines a function called `count_distinct_characters` that calculates the number of distinct characters in a given string. The test suite contains several test cases that verify the correctness of this function.