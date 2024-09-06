```python
def split_words(txt):
    ans = txt.split(',') if ',' in txt else txt.split() if ' ' in txt else len([x for x in txt if x.islower() and ord(x) % 2 == 0])
    return ans
```

The code solves the problem by performing the following steps:
1. Checks if the string contains a comma ',' by querying if the string contains one or more commas, using the `','` regex syntax.
2. If the string contains commas, it uses the `split()` method to split the string into a list on comma boundaries.
3. If the string does not contain commas, it checks if it contains spaces ' ' by querying if the string contains one or more spaces.
4. If the string contains spaces, it splits the string into a list on space boundaries using the `split()` method.
5. If the string contains no spaces or commas, it finds the number of lowercase letters with an even ASCII order and returns their count as the list.

The code efficiently solves the problem using string manipulation methods and regex queries, providing the required output based on the input string contents.