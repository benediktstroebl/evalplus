```python
def concatenate(strings: List[str]) -> str:
    return "".join(strings)

def test_concatenate():
    assert concatenate([]) == "", "Should return empty string for an empty input"
    assert concatenate(["a"]) == "a", "Should return a single string"
    assert concatenate(["a", "b"]) == "ab"
``` 
This script defines a function **`concatenate`** that takes a list of strings and returns their concatenation as a single string. It also includes a test function **`test_concatenate`** with assert statements that check the correctness of the **`concatenate`** function with different input scenarios.