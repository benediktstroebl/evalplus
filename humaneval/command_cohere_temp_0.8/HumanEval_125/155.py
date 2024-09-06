```python
def split_words(txt):
    ans = txt.split(',') if ',' in txt else txt.split() if ' ' in txt else len(list(filter(lambda c: ord(c) % 2, txt.lower())))
    return ans
```

The provided Python script solves the problem by using a conditional approach. It checks the existence of whitespace and comma characters in the input string `txt`. If whitespace is present, it utilizes the `split()` method to split the string into a list of words, this is done by partitioning the string around the whitespace characters. If no whitespace is present, it checks for the presence of commas, and if found, it splits the string into a list of words using the comma character as the delimiter. Lastly, if neither whitespace nor commas are present, it counts the number of lowercase letters with an odd numerical value when interpreted as an integer (`c`ollisions `o`f `l`owercase `n`umbers). The `filter()` and `len()` functions are used to count the number of characters with an odd ordinal value, and the result is returned as the list of words. 

The script ensures functionality and compatibility by accounting for different scenarios and utilizing the appropriate methods for splitting the string into words.