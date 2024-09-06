```python
def split_words(txt):
    ans = txt.split(',') if ',' in txt else txt.split() if ' ' in txt else len([x for x in txt if x.isalpha() and x.lower() not in 'abcdefghijklmnopqrstuvwxyz'])
    return ans
```
The function takes an input string and checks if the string contains spaces by using the `split()` method. If the string does not contain spaces, it checks if the string contains a comma by using the `split()` method. If neither is present, it checks the number of lowercase letters that are not in alphabetical order. It then returns the number of letters in the string that are not in alphabetical order. If commas are present, it returns the string split on commas. If spaces are present, it returns the string split on spaces.