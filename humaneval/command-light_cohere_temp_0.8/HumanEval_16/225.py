Here's the improved Python script:
```python
def count_distinct_characters(string: str) -> int:
    distinct_characters = set(string.get().lower())
   
    return len(distinct_characters)

# Unit tests
def test_count_distinct_characters():
    assert count_distinct_characters('abc') == 3    # Contains only lowercase 'a'
    assert count_distinct_characters('XYZ') == 3    # Contains only lowercase 'x'
    assert count_distinct_characters('jerry') == 4    # Contains mixed case characters
    assert count_distinct_characters('abcXYZ') == 3   # Contains only lowercase
```
The code defines a function **`count_distinct_characters`** that accepts a string **`string`** as an argument. The function utilizes the string. The **`set()`** method is applied to all lowercase characters in the string. This generates a distinct characters set. The count of distinct characters is then returned by the function. The unit tests test the simple assertions to confirm the functionality of the **`count_distinct_characters`** function. The purpose of this is to evaluate the correctness of the function.