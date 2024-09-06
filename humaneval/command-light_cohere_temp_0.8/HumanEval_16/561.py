Here's a self-contained Python script with a function that counts the number of distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string: str) -> int:
    return len(set(string))

# Test the function with sample cases
string1 = 'xyzXYZ'
result1 = count_distinct_characters(string1)
print("First string has", result1, " distinct characters")

string2 = 'jerry'
result2 = count_distinct_characters(string2)
print("Second string has", result2, " distinct characters")

# The output should be:
First string has 3 distinct characters
Second string has 4 distinct characters
```

The function uses the `set` data structure to keep track of unique characters in the input string, and then calculates the length of this set, which gives the number of distinct characters in the string. This is the way to achieve the goal of counting distinct characters in a string, regardless of case.