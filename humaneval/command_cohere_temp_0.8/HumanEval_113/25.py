```python
def odd_count(lst):
    r = [str(len(re.findall(r'1|3|5|7|9', s)))
         .replace('1', 'the number of odd elements in the string ')
         .replace('0', 'the number of even elements in the string ')
         .replace('4', 'the string ')
         for s in lst]
    return r
```

The above `odd_count` function uses the regex expression `r'1|3|5|7|9'` to find all odd digits in a given string, and then replaces them with '1', '3', '5', '7', and '9' to determine the number of odd elements in a string. The final result is a list of strings containing the number of odd elements in each string.