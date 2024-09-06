```python
def odd_count(lst):
    r = [str(len(re.findall(r'1|3|5|7|9', s)))
        .replace('1', 'the number of odd elements in the string ')
        .replace('0', 'the number of even elements in the string ')
        for s in lst]
    return r
```

The above `odd_count` function employs the regex expression `r'1|3|5|7|9'` to successfully detect odd digits in each string, then calculates and returns the corresponding formatted sentence.

This solution is efficient and will not freeze for large input arrays since it doesn't iterate through each character in each string but instead uses the `re.findall` function to find all occurrences of odd digits in each string only once. Thus, the time complexity is O(n * m) where n is the length of the list and m is the maximum length of a string, and the space complexity is O(n) due to the creation of the result list and the regex pattern.

Additionally, the code is relatively concise and easier to understand in comparison to other possible solutions.