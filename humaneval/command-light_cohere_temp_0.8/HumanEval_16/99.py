```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.count(char)
    return len(characters)

# Test case 1: Regular string
test_case1 = "xyzXYZ"
result_test_case1 = count_distinct_characters(test_case1)
assert result_test_case1 == 3

# Test case 2: Username input
test_case2 = "Jerry"
result_test_case2 = count_distinct_characters(test_case2)
assert result_test_case2 == 4
``` 
This Python function uses the set data structure to count unique characters in a given string. The function then returns the number of distinct characters in the passed string.