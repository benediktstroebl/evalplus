```python
def odd_count(lst):
    r = [str(len(re.findall(r'1|3|5|7|9', s)))
         for s in lst]
    return ['the number of odd elements in the string %s of the input.'%i
            for i in r]
```

This code uses the regex expression `r'1|3|5|7|9'` to match all odd digits and then uses `re.findall()` to count how many of those odd digits are in each string. Finally, it creates a string template and inserts the counts into it to produce the desired result.