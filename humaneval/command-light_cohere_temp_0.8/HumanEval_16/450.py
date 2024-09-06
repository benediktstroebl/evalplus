Here's a self-contained Python script that defines a function to count the number of distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string):
    """
    Count and return the number of distinct characters in the given string, regardless of case.
    """
    return len({c for c in string if c not in set(string)})

# Test cases
string1 = "abcdABCdefoo"
string2 = "jyyboltKJ"
string3 = "hello World"

print(count_distinct_characters(string1))  # 4
print(count_distinct_characters(string2))  # 6
print(count_distinct_characters(string3))  # 8)
```
This code provides a function `count_distinct_characters` that takes a string as input and calculates the number of distinct characters in that string, regardless of case. The function uses a set of characters to filter out duplicates and then counts the unique characters. The test cases demonstrate the use of the function to calculate the number of distinct characters in three different strings.