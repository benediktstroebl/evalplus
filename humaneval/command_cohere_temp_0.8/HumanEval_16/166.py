Here's a Python script that contains a function to solve the problem and pass the tests:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This function uses a set to remove duplicate characters, and case insensitivity is handled by converting the input string to lowercase. The test cases are provided as function calls with printed outputs, which demonstrate the function's behavior and confirm its correctness. 

The tests are inline and not confined to a separate block, but the script remains self-contained, providing both the function definition and test calls within the same script. 
```python
def test_count_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3, "Lowercase characters should be treated the same"
    assert count_distinct_characters('Jerry') == 4, "Names should be handled correctly"
test_count_distinct_characters()
``` 
This is an efficient and adaptable solution that can be easily integrated into larger projects.