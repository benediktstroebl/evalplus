Here's the Python code to solve the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This function uses a set data structure to remove duplicate characters and ensures that the count is correct regardless of the case. 
The tests will prove the correctness of the function. 
```python
def test_count_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('Jerry') == 4
    assert count_distinct_characters('helloWorld') == 6
    assert count_distinct_characters('AAAbbbbb') == 6
    assert count_distinct_characters('pokerhero') == 5
    assert count_distinct_characters('Python') == 4
```