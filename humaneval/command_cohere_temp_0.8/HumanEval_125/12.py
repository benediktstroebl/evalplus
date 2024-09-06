```python
def split_words(txt):
    ans = txt.split(',') if ',' in txt else txt.split() if ' ' in txt else len([x for x in txt if x.isalpha() and x.lower() not in 'abcdefghijklmnopqrstuvwxyz'])
    return ans
```
The function takes an input string and checks if the string contains spaces by using the `split()` method on a comma ``,` if no commas are found. The idea is to split the string into a list of words, where each word is a substring of the original string separated by whitespace. If the string doesn't contain any whitespace or commas, it calculates the number of lowercase letters with odd alphabetical order. The function returns the list of words or the number of letters with odd order accordingly.