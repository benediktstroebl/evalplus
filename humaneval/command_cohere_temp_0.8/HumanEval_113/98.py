```python
def number_of_odd(lst):
    r = []
    for num in lst:
        odd = sum(1 for c in num if c % 2 != 0)
        r.append(f"the number of odd elements {odd}n the str{len(num)}ng {num} of the input.")
    return r
```

The solution leverages Python's sum function with a generating expression to tally the count of odd digits, which is then employed to construct the desired output string. 

This problem can also be solved using Python's built-in `str.format` method to construct the output strings, as shown in the code block below:
```python
def number_of_odd(lst):
    r = []
    for num in lst:
        odd = sum(1 for c in num if c % 2 != 0)
        r.append(f"the number of odd elements {odd}n the string {num} of the input.")
    return r
```

This method simplifies the string construction by using placeholders (`{odd}` and `{num}`) and then passes them to the `format` method. 

Both approaches produce the desired output, and the choice between them depends on personal preference and the complexity of the challenge at hand.