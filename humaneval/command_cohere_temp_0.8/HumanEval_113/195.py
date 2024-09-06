```python
def odd_count(lst):
    r = [str(len(re.findall(r'1|3|5|7|9', s)))
         .replace('1', 'the number of odd elements in the string ')
         .replace('0', 'of the ')
         .replace('1', '1n')
         .replace('3', '3n')
         .replace('5', '5n')
         .replace('7', '7n')
         .replace('9', '9n')
         for s in lst]
    return r
```

The function uses a list comprehension that calculates the length of the findall result for each digit string in the input list. The `re.findall` method searches for all occurrences of the target pattern in the input string. In this case, the pattern '1|3|5|7|9' looks for all odd digits. The replacement strings in the formulation of the problem are implemented in the `replace` methods so that the output list contains the desired human-readable form with the placeholder i replaced by the number of odd digits.