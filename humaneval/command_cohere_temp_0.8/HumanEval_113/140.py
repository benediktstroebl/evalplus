```python
def odd_count(lst):
    r = [str(len(re.findall(r'1|3|5|7|9', s)))
         .replace('1', 'n')
         .replace('3', 'n')
         .replace('5', 'n')
         .replace('7', 'n')
         .replace('9', 'n')
         for s in lst]
    return r
```

The function uses a list comprehension that iterates through each string in the list and counts the number of odd digits using the regular expression `re.findall(r'1|3|5|7|9', s)`. The replacement field of the list comprehension then replaces each digit string with a string stating the number of odd digits and using the corresponding replacement fields. The result is a list of these modified strings.