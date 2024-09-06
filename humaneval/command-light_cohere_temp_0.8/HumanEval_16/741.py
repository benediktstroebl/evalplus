```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string. characters()})

def test_distinct_characters():
    assert count_distinct_characters('abc') == 3
    assert count_distinct_characters('xyZW') == 3
    assert count_distinct_characters('XYZ') == 3
    assert count_distinct_characters('jerry') == 4
    assert count_distinct_characters('  jerry  ') == 4
    assert count_distinct_characters('   jerry  ') == 4
```
The code defines a function **count_distinct_characters** that calculates the count of unique characters in a given string. 

The function uses a generator expression along with the **len** function to count unique characters and returns the count as an integer. 
The **test_distinct_characters** function contains assertions that verify the correctness of the **count_distinct_characters** function for different input strings.