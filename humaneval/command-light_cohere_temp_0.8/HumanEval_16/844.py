```python
def count_distinct_characters(string: str):
    return len([c for c in string.s.lower() if c in string])

# Test cases
assertEqual(count_distinct_characters('xyzXYZ'), 3)
assertEqual(count_distinct_characters('jerry'), 4)
assertEqual(count_distinct_characters('JERBY'), 4)
assertEqual(count_distinct_characters(''}, 5)
assertEqual(count_distinct_characters(''xosome'), 8)
``` 
This code defines a function `count_distinct_characters` that calculates the number of distinct characters (ignoring case) in the given string. It then tests these function's correctness by comparing its output with the expected results for various input strings using `assert`.  The function returns an integer count of distinct characters.