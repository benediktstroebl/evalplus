Here is a self-contained Python script that defines a function to count the number of distinct characters in a given string:
```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.string() if c.isdigit()})

def test_distinct_characters(string: str) -> None:
    assert count_distinct_characters("abc") == 3
    assert count_distinct_characters("123") == 3
    assert count_distinct_characters("XyX") == 3
    assert count_distinct_characters(" Jerry ") == 4
    assert count_distinct_characters("  hi  ") == 4
    assert count_distinct_characters("  jerry  ") == 4
    assert count_distinct_characters("   \t\n123\r\f") == 5
    assert count_distinct_characters("ocks") == 3
    assert count_distinct_characters("QWERTYUIOPASDFOH") == 13
    assert count_distinct_characters(" ") == 0
    assert count_distinct_characters("X") == 0
``` 
The first function, `count_distinct_characters`, takes a string as input and returns the count of distinct characters in the string. The function uses a list comprehension to filter out duplicate characters and count them. The test_distinct_characters function provides test cases to verify the functionality of the `count_distinct_characters` function.