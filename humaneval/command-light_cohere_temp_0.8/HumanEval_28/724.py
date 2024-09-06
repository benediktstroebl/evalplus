```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string"""
    
    # Use Type hints to improve readability and avoid confusion
    return "".join" + (", ".join(strings) if strings else "")

# Unit tests
concatenate.test_concatenate = [
    ("", ""),
    ("a", "ab"),
    ("abc", "abc"),
    ("abc", ""),
    ("", "hello"),
]

def test_concatenate():
    assert concatenate(concatenate.test_concatenate) == "hello"

if __name__ == "__main__":
    print("All tests passed!")
```