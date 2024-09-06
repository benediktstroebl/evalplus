```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string. string() if c.isalpha()})

    # Test cases
assertEqual(count_distinct_characters('xyzXYZ'), 3)
assertEqual(count_distinct_characters(' Jerry'), 4)
assertEqual(count_distinct_characters(' abilities Unlimited'), 7)
assertEqual(count_distinct_characters('A B C'), 6)
```  This script defines a function that counts the number of distinct characters in a given string, regardless of case. The function uses a itertools.hash of characters in the unique characters in the string and returns the count. It also includes some series of tests to verify the correctness of the function.