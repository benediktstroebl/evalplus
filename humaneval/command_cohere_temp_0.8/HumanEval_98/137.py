Here's the Python script with a function that solves the problem:
```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    vowels = set(['A', 'E', 'I', 'O', 'U'])
    count = 0
    for i in range(0, len(s), 2):
        if s[i].isupper() and s[i] in vowels:
            count += 1
    return count
```

This script defines a function `count_upper()` that takes a string `s` as input and counts the number of uppercase vowels in even indices. It uses a set called `vowels` to efficiently check if the letter is a vowel and checks if the letter in the current index is in an even position before checking if it's an uppercase vowel. The total count is returned at the end. 

The example tests provided earlier will demonstrate the functionality of this script. Let me know if you'd like me to provide further clarification or additional examples to illustrate the robustness of this solution.