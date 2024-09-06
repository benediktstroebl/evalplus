```python
def odd_count(lst):
    r = [str(len(re.findall(r'1|3|5|7|9', s)))
        .replace('1', 'the number of odd elements in the string ')
        .replace('0', 'the number of even elements in the string ')
        for s in lst]
    return r
```

The above `odd_count` function uses the regex expression `r'1|3|5|7|9'` to find all the odd digits and then replaces the index-related strings with the count of odd digits in the strings. The resulting string is returned as a list, as specified in the problem statement. You can test the above function using the given test cases to verify its behavior and assert its correctness.  This approach clearly showcases the use of regex to solve the problem effectively.