```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test the function with different inputs and expected outputs
strings_test = ['abc', 'bacd', 'cde', 'array', 'hello']
substring_test = 'a'

# Call the function and compare the result with the expected output
result_test = filter_by_substring(strings_test, substring_test)

print("Test 1 Result:", result_test)
print("Test 1 Expected Output:", [['abc', 'bacd', 'array'])")

# Again, to make it clear
strings_test = ['abc', 'bacd', 'cde', 'array', 'hello']
substring_test = 'cde'

# Call the function again and compare with the expected output
result_test = filter_by_substring(strings_test, substring_test)

print("Test 2 Result:", result_test)
print("Test 2 Expected Output:", [['cde'])
```

This code defines a function `filter_by_substring` that takes a list of strings and a substring as input and returns a new list containing only the strings that contain the given substring. The function is then tested with two different sets of strings and substrings.