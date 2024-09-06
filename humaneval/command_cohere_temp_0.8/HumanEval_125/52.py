```python
def split_words(txt):
    words = txt.split(',') if ',' in txt else txt.split() if ' ' in txt else len(list(filter(lambda c: c.islower(), txt))) % 2 == 0
    return words
```

The problem asks to return the list of words split on whitespace, if no whitespace exists in the text, it should split on commas instead. If neither whitespace nor commas exist in the text, return the number of lowercase letters with odd order in the alphabet. The function splits the string on whitespace if it exists, otherwise, it splits the string on commas. If neither whitespace nor commas are present in the text, it returns True if the number of lowercase letters is odd, False otherwise. 

It is a good practice to solve problems like this by extracting the relevant criteria and handling them step by step. One way to do this is by using boolean variables that reflect the applicability of each criterion to the given text. This way we can comfortably execute different code blocks depending on the criteria evaluated: 
```python
def split_words(txt):
    whitespace_exists = ' ' in txt
    comma_exists = ',' in txt
    if whitespace_exists:
        return txt.split()
    elif comma_exists:
        return txt.split(',')
    else:
        odd_lowercase = len(list(filter(lambda c: c.islower(), txt))) % 2 == 0
        if odd_lowercase:
            return [True]
        else: 
            return [False]
```