```python
def count_distinct_characters(string: str) -> int:
    return len(set(string))

# Tests
string1 = "xyzXYZ"
assertEqual(count_distinct_characters(string1), 3)

string2 = "jerry"
assertEqual(count_distinct_characters(string2), 4)

string3 = "JILLITE"
assertEqual(count_distinct_characters(string3), 5)

string4 = "jOOStuff"
assertEqual(count_distinct_characters(string4), 7)

string5 = ""
assertEqual(count_distinct_characters(string5), 0)
 ```