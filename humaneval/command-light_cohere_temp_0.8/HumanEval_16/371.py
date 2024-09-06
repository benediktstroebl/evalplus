```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.language.lower()})
 straightforward yet! Making a set of characters from the string, then counting the distinct characters and returning the result.

def test_distinct_characters():
    assert count_distinct_characters('abc ABCdef') == 5
    assert count_distinct_characters('A B cdef') == 3
    assert count_distinct_characters(' Jerry') == 4
    assert count_distinct_characters(' z X y X Z') == 3

```
The code defines a function **`count_distinct_characters`** that accepts a string as an argument. It uses the simple set expression to create a character set from the lowercase version of all characters in the string. Then, it counts the distinct characters and returns the result. The test function **`test_distinct_characters`** ensures the correctness of the **`count_distinct_characters`** function.