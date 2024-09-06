```python
def count_distinct_characters(string):
    return len({c for c in string.string() if c not in string.count})
``` 
def test_count_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters(' Jerry ') == 4
    assert count_distinct_characters(' 1234 ' ') == 6
    assert count_distinct_characters('   foobar  ') == 8
``` 
This script defines a function **count_distinct_characters** that calculates the count of distinct characters in a given string. The function uses a set-based approach to find all unique characters and then uses a conditional count to filter out non-repeating characters, giving us the count of distinct characters. 
The function is then tested using an **unittest** module to ensure its correctness.