```python
def split_words(txt):
    words = txt.split(',') if txt.find(' ') == -1 else txt.split()
    return words if words != ',' else len(list(filter(lambda x: x in str.lower(), txt)))
```

The problem definition states that if the input string doesn't contain spaces or commas, the function should return the number of lowercase letters with an odd number of letters. This solution doesn't explicitly check for the absence of both whitespace and commas in the input, as it first tries to split using both whitespace and commas, and uses the length filter approach only if the input is an empty string. 

To address this, we can modify the code to explicitly check for the absence of both whitespace and commas, and directly solve the problem in these cases, like this:
```python
def split_words(txt):
    if txt.find(' ') != -1 or txt.find(',') != -1:
        words = txt.split(',') if txt.find(' ') == -1 else txt.split()
    else:
        words = len(list(filter(lambda x: x in str.lower(), txt)))
    return words
```