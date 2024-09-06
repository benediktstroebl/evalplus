```python
def same_chars(s0, s1):
    return len(set(s0) & set(s1)) / min(len(s0), len(s1)) > 0.6
```

The function works by calculating the Jaccard index of the two strings, which measures the similarity between two sets, in this case, the sets of unique characters present in the two input strings. The Jaccard index is calculated by finding the intersection of the two sets (the shared unique characters) and dividing it by the minimum of the two set sizes (the minimum length of the input strings). If the result is greater than 0.6, it returns True, otherwise, it returns False.

It's a concise and accurate way of solving the problem, ensuring that the function is self-contained and doesn't rely on external variables or assumptions outside of what's given in the input.