Here's a Python script with a self-contained function that solves the problem:
```python
def same_chars(s0, s1):
    return len(set(s0) & set(s1)) / min(len(s0), len(s1)) > 0.6
```
This solution utilizes set theory to efficiently compare characters of two strings irrespective of their length and structure. It calculates the shared characters' ratio to the minimum of the lengths of the two strings, resulting in a score exceeding 0.6 denoting a substantial similarity.