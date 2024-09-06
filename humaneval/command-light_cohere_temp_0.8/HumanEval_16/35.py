```python
def count_distinct_characters(string: str) -> int:
    characters = set(string)
    return len(characters)

# Test the function with example inputs
test_count_distinct_characters = lambda: [
    assert count_distinct_characters('abc') == 3, "Should get 3 distinct characters"
    assert count_distinct_characters(' abc 123 XYZ abc') == 6, "Should get 6 distinct characters"
    assert count_distinct_characters(' jerry') == 4, "Should get 4 distinct characters"
)(
if __name__ == "__main__":
    test_count_distinct_characters()
```
This code defines a function `count_distinct_characters` that calculates the count of distinct characters in a given string, regardless of case. It then includes a test function to verify the correctness of the code with a series of asserts. The test function evaluates the example inputs and ensures that the function produces the expected results.