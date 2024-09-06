Here's a Python script with a self-contained function that solves the problem:
```python
def same_chars(s0, s1):
    return len(set(s0) & set(s1)) / min(len(s0), len(s1)) > 0.6
```
This solution utilizes set theory to accurately assess the presence of shared characters, irrespective of their positional occurrence in the input strings. It then calculates the ratio of shared characters, returning True if this falls above a threshold of 60%.