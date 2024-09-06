Here is a self-contained Python script with a function that solves the problem of returning the longest string from a list of strings:

```python
from typing import List
def longest(strings: List[str]) -> str:
    """ Out of list of strings, return the longest one. """
    return max(strings, key=len)

# Example usage
strings = ['a', 'b', 'c']
print(longest(strings))  # Output: 'c'
```

Let's go through the code step by step:

1. Input parameter: `strings: List[str]` is defined as the list of strings. This parameter allows us to pass a list of strings as an argument to the `longest` function. 

2. `def longest(strings: List[str]) -> str:` This line defines a function named `longest` that takes a list of strings as an argument. The function returns a type of the string that is the longest one in the list.

3. `return max(strings, key=len)`: This line uses the `max` function from the `builtins` library to find the maximum value in the list of strings. The `key` parameter is set to `len` to specify that the index of the string is used as the key to compare for maximum. 

4. `strings`: The _ the list of strings passed to the `longest` function.

5. `print(longest(strings))`: This line calls the `longest` function with the `strings` argument, and the result is printed to the console.