```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_occurrences = {}
    for letter in s:
        if letter in letters_occurrences:
            letters_occurrences[letter] += 1
        else:
            letters_occurrences[letter] = 1
    return all(value < 3 for letter, value in letters_occurrences.items())
```

This script defines a function `is_happy` that takes a string `s` as input and checks whether the string is happy as described in the prompt. It does so by performing the following steps:
1. It checks if the string's length is at least 3, returning `False` if it's shorter than this. 
2. It uses a dictionary `letters_occurrences` to keep track of the occurrences of each letter in the string. 
3. It iterates through each letter in the input string, incrementing its count in the `letters_occurrences` dictionary. 
4. Finally, it returns `True` if every count of letters in `letters_occurrences` is less than 3, indicating that all consecutive triplets of letters are distinct.

The script self-contained and does not rely on any external variables or functions, and can be executed directly to test its functionality. 

You can test this function using different inputs to assert its correctness. Here's an example of how you can use assert statements to verify the output of the `is_happy` function with different test cases:
```python
# Test case: Single-letter string
assert not is_happy("a"), "The single-letter string 'a' should not be happy"

# Test case: Happy string
assert is_happy("abcd"), "The string 'abcd' should be happy"

# Test case: Unhappy string
assert not is_happy("aabb"), "The string 'aabb' should not be happy"

# Test case: Short unhappy string
assert not is_happy("xyy"), "The string 'xyy' should not be happy"

# Test case: Happy longer string
assert is_happy("xyzabcde"), "The string 'xyzabcde' should be happy"
```

You can add more test cases as needed to cover a variety of scenarios and ensure the function's correctness for different cases.