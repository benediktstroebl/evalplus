```python
def count_distinct_characters(string):
    return len(set(string.count(c for c in string if c.isalpha()))
``` 
Sure, this script defines a function that calculates the number of distinct characters in a given string, regardless of case. It also provides test the follow-up test cases: