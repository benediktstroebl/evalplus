Here's the self-contained Python script with a function that calculates the number of distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string: str) -> int:
    return len(set(string.lower()))
```
The function uses the `set()` and `lower()` methods to remove case sensitivity and create a set of distinct characters in the input string, which then calculates its length to return the number of distinct characters.

The test code provided earlier is a good example of how to use this function to solve the problem, and the function passes the test.

Let's break this down:
1. **Function Definition**: Defines a function named `count_distinct_characters` that takes a string as its argument and returns an integer. The function aims to determine the number of distinct characters (case-insensitive) in the input string.
2. **Set of Distinct Characters**: Within the function, a set is created using the `string.lower()` method, which converts all characters in the string to lowercase. This set will contain all distinct characters in the original string.
3. **Length of the Distinct Characters**: The length of the set is then calculated using the `len()` function. This length value represents the all distinct characters, regardless of their original case.
4. **Return Value**: The function returns the integer value of the length of the set as its output.

In essence, this function is self-contained and efficiently calculates the count of distinct characters in the provided string, without relying on external methods or functions. It demonstrates the principles of clean and readable code, and can be easily adapted or extended to solve other problems related to character counts or sets.