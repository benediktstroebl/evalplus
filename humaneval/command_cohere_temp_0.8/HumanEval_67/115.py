```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

The fruit_distribution function takes a string and an integer as input, parses the string into an integer representation of apples and oranges, and returns the number of mangoes based on the provided formula. This solution leverages basic Python string and integer handling capabilities to accomplish the task. 

Let's break down the solution step by step:
1. **Function Definition**: We define a function named `fruit_distribution` that takes two parameters: `s` (a string) and `n` (an integer).
2. **String Splitting**: The line `apples, oranges = map(int, s.split(' and '))` is a bit tricky. It uses a few Python features together. Here's what it does:
 - `s.split(' and ')` splits the string `s` using the delimiter ' and '. This splits the string into a list of substrings.
 - `map(int, ...) ` transforms each element in the list of substrings into an integer.
 - `..., apples, oranges = ` assigns the results of the mapping process back to the variables `apples`, `oranges`.
This means `apples` and `oranges` now hold the extracted integer values from the string.
3. **Calculation**: Finally, the function returns `n - apples - oranges`, which provides the number of mangoes in the basket, following the problem statement's logic.

This solution is concise and efficient, and it demonstrates Python's capabilities for string manipulation and basic arithmetic operations.