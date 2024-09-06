```python
def split_words(txt):
    ans = txt.split(',') if ',' in txt else txt.split() if ' ' in txt else len([x for x in txt if x.islower() and ord(x) % 2 == 0])
    return ans
```

The problem asks us to split a string of words into individual words using whitespace or commas as separators. If the string contains no whitespace or commas, the function is supposed to return the count of lowercase letters with an even number of letters. Using Python's built-in split() function, we can achieve this depending on if the string contains whitespace or commas as separators. Handling the case with no separators, we iterate through the string looking for lowercase letters with an even number of letters, as this condition satisfies the given condition in the problem. We then return the answer to the given problem as a list of strings or an integer depending on the conditions stated.