Here's a Python script with a self-contained function that solves the problem:
```python
def same_chars(s0, s1):
    return len(set(s0) & set(s1)) / min(len(s0), len(s1)) > 0.6
```
The function works by comparing the unique characters in both strings and checking whether common characters make up at least 60% of the shorter string length. The markdown code block is also included to maintain code readability.

This solution relies on the assumption that repeated characters will have a significant impact on the result. It may not work optimally for strings with rare characters or differing character frequencies.