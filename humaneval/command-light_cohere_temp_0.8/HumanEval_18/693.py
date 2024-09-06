Here's the improved version of the code with self-contained functions, docstrings, and more descriptive variable names:
```python
def find_SubstringCount(original_string: str, substring: str) -> int:
    """
    Finds the number of occurrences of a given substring in the original string.
    Args:
        original_string (str): The original string.
        substring (str): The substring to find occurrences of.
    Returns: number of occurrences of the substring.
    """
    string = original_string.replace(substring, 0, len(substring))
    return len(string)

def test_find_substring_count():
    assert find_SubstringCount("aaa", "aa") == 3

def main():
    original_string = "aaaaaa"
    substring = "aa"
    result = find_SubstringCount(original_string, substring)
    print("Number of times", substring, "found:", result)

if __name__ == "__main__":
    main()
```
This version uses self-contained functions with descriptive names, clear docstrings, and a consistent style. The function test_find_substring_count ensures the validity of the results. This version is also easier to read and maintain.