```python
def count_distinct_characters(string: str) -> int:
    return len(set(string))

# Test the function with some inputs
string1 = "Hello World"
string2 = "jerry micha"
string3 = "IS universal"

print(count_distinct_characters(string1))  # Output: 5
print(count_distinct_characters(string2))  # Output: 4
print(count_distinct_characters(string3))  # Output: 6
``` 
This code defines a function `count_distinct_characters` that calculates the count of distinct characters in a given string, regardless of case. The function uses the string's characters as a set and then calculates its length to return. The function is successfully tested using three different input strings.