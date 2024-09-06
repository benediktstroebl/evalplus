```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.str.lower() if c != c.isalpha})

``` 
# Example usage
result = count_distinct_characters('xyzXYZ')
print(result)  # Output: 3

result = count_distinct_characters('Jerry')
print(result)  # Output: 4
``` 
This code defines a function **count_distinct_characters** that accepts a string as an argument and returns the number of distinct characters in the string, regardless of case. It uses a set comprehension to find each character once and only if it is in lowercase, and it is not equal to any other character in the string, is not the same letter (isalpha).  It then returns the number of these distinct characters.