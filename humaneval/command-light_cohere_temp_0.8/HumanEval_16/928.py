```python
def count_distinct_characters(string: str) -> int:
    return len(set(string.lower()))
```
Here's the explanation :
- The `count_distinct_characters` function takes a string as an argument.
- Inside the purpose is to count the distinct characters in a given string, regardless of their case. 
- The function converts the input string into a lowercase string using the `lower()` method.
- Then then use the `len` function to get the length of the resulting set.
- The resulting set contains all the distinct characters in the lowercase string, and its length is returned as the result of the function.

The provided code is self-contained and defines a function that solves the problem and passes the tests. It utilizes the set and the `lower()` method to achieve this.