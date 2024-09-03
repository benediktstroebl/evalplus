```python
def same_chars(s0, s1):
    return len(set(s0) & set(s1)) / min(len(s0), len(s1)) > 0.6
```

The function works by calculating the Jaccard index of the two strings, which measures the similarity between two sets, in this case, the set of characters in each string. The Jaccard index is calculated by finding the size of the intersection of the two sets (the characters present in both strings) and then dividing it by the size of the union of the two sets (the total number of unique characters in both strings), multiplied by each other. The resulting value is a number between 0 and 1, where 1 indicates that all the characters in one string are also present in the other string, and 0 indicates that none of the characters overlap.