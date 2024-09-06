Here's a Python script with a function that solves the problem:
```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    vowels = 'AEIOU'
    count = 0
    for i in range(0, len(s), 2):
        if s[i].isupper() and s[i] in vowels:
            count += 1
    return count
```

This function defines a list of uppercase vowels to use as a reference, iterates through the passed string s at even indices, and counts the number of indices containing an uppercase vowel. It then returns the count of uppercase vowels in even indices. 

It is efficient with a time complexity of O(n), where n is the length of the input string s. This is because it iterates through the string exactly once, and each iteration increments the index by 2, checking only every second index. It also has a space complexity of O(1) since it does not require any additional storage aside from the variables utilized in the function.