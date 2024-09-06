```python
def same_chars(s0, s1):
    return len(set(s0) & set(s1)) / min(len(s0), len(s1)) > 0.6
```

The function leverages the similarity threshold of more than 60% of characters between two strings to determine if they have a "substantially" similar character set, albeit with some flexibility due to potential differences in character frequency. 

To better understand the logic of the function and how it achieves the goal of the prompt, let's break it down step by step:
1. **Defining the Function**: The function same_chars takes two arguments, s0 and s1, which are two strings that we want to compare.
2. **Set Operations**: The function utilizes set operations to efficiently compare characters. By taking the intersection of the sets formed from each string, the code identifies common characters between the two input strings.
3. **Character Frequency**: Next, the function considers the minimum length between the two strings, as well as the ratio of common characters to this minimum length. This ratio calculates the fraction of characters that are shared between the two strings.
4. **Threshold**: The condition len(set(s0) & set(s1)) / min(len(s0), len(s1)) > 0.6 is a threshold check. If the ratio of common characters to the shorter string length is greater than 0.6, the function returns True, indicating that the strings have substantially the same characters. Otherwise, it returns False.

This approach provides a flexible and efficient solution to the problem, as it handles varying lengths and character frequencies in strings.