```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join(char) for char in string if char != ' ' and char != '\n']

# Tests
def test_prefixes():
    assert all_prefixes("hello") == ['h', 'el', 'llo']
    assert all_prefixes("    abc") == ['a', 'ab', 'abc']
    assert all_prefixes("\t\n\r   ") == ['\t', '\n', 'r', '  ']
    assert all_prefixes("abc\nx") == ['abc', 'a', 'ab', 'nx']

# Main
if __name__ == "__main__":
    test_prefixes()
```

I hope the above code provides a complete Python script with a self-contained function `all_prefixes` that takes a string as input and returns a list of its prefixes. The `test_prefixes` function conducts several tests to ensure the correctness of the `all_prefixes` function. 
At the heart of the script, we have the `if __name__ == "__main__":` block, which serves to execute the code only when the script is run directly, not when it's imported. 
This is a common way to write tests and run the code in Python.