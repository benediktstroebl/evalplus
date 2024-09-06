```python
def cycpattern_check(first, second):
    return second in rotated_substrings(first)

def rotated_substrings(string):
    substrings = [string[i:] for i in range(len(string) + 1)]
    substrings += [string[:i] for i in range(1, len(string) + 1)]
    return substrings
```

The `cycpattern_check` function takes two strings as input and checks whether the second string is a rotated substring of the first string. It does this by leveraging the `rotated_substrings` helper function, which generates all possible rotated substrings of a given string and returns them in a list.

The `rotated_substrings` function takes a string as input and creates all possible rotated substrings using two list comprehensions. The first comprehension removes the first character and creates a substring from the remaining characters, while the second comprehension creates a substring from the first character and the remaining characters. These two comprehensions generate all possible rotated substrings of the given string.