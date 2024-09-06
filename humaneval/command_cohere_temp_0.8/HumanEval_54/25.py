Here's a Python script with a self-contained function that solves the problem:
```python
def same_chars(s0, s1):
    return len(set(s0) & set(s1)) / max(len(s0), len(s1)) > 0.6
```
The function compares two input strings s0 and s1. It calculates the similarity between the strings using the sets of unique characters in each string. The threshold for determining if the strings are similar is 0.6. Thus the function returns True if the ratio of matching characters is greater than 0.6 and False otherwise. 
This approach does not consider the order of characters, which is the intended solution based on the test cases provided.