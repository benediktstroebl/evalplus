Here is a self-contained Python script with a function that solves the problem of counting distinct characters in a given string:
```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string. string()})
```
# Tests
def test_distinct_characters():
    assert count_distinct_characters('abc') == 3
    assert count_distinct_characters('XyXuYY') == 4
    assert count_distinct_characters(' jerry') == 4

# Main execution 
if __name__ == "__main__":
    print("Starting the program...")
    test_distinct_characters()
    print("Program ended successfully.")
```
The provided code defines a Python function `count_distinct_characters` that calculates the count of distinct characters in a given string. The function utilizes a list comprehension and a dictionary to achieve this. The code also includes a test function `test_distinct_characters` with test cases that verify the correctness of the `count_distinct_characters` function. 
Finally, the `main` block ensures that the tests are run before the program ends.