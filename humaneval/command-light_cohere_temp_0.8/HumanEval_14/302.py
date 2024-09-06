```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join[i for i, char in enumerate(string, 1) if char != " " and i != 0]

# Test cases
test_cases = [
    ("abc", ["a", "ab", "abc"]),
    ("hello world", ["h", "ello", "orld"]),
    ("javascript:", ["js", "v", "ascript"])
]

def test_function():
    assert all_prefixes("abc") == ["a", "ab", "abc"]
    assert all_prefixes("hello world") == ["h", "ello", "world"]
    assert all_prefixes("javascript: ") == ["js", "v", "ascript"]

def main():
    test_function()

if __name__ == "__main__":
    main()
``` 
This Python code is a self-contained solution to the problem of returning all prefixes from shortest to longest of the input string. It uses the Python's typing module and a function named `all_prefixes`. The function uses a list comprehension to iterate through the characters of the input string, starting from the second character (index 1) to check if the character is not space and if the index is not 0. The function returns a array of all prefixes found. The test cases section uses the `assert` to check if the `all_prefixes` function returns the expected results for different input strings.