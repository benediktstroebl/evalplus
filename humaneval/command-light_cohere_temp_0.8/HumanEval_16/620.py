```python
def count_distinct_characters(string: str):
    return len(set(string))

# Tests
string1 = 'xyXyzY'
assert count_distinct_characters(string1) == 3

string2 = 'jerry'
assert count_distinct_characters(string2) == 4

string3 = '123'
assert count_distinct_characters(string3) == 8

```
This code defines a function called `count_distinct_characters` that computes the number of distinct characters in a given string. It uses the `set()` function along with the `string` to create a set of characters and then calculates its length. The test section ensures the test cases work correctly by asserting the output against different inputs.