```python
def count_consonants(word):
    """Count consonants in a word"""
    word = word.lower()
    total = 0
    for char in word:
        if char in "bcdfghjklmnpqrstvwxyz":
            total += 1
    return total

def select_words(s, n):
    """Return list of words containing exactly n consonants"""
    words = s.split()
    result = []
    for word in words:
        consonant_count = count_consonants(word)
        if consonant_count == n:
            result.append(word)
    return result
```
The `count_consonants` helper function calculates the number of consonants in a given word, while the `select_words` function splits the input string into a list of words and then iterates through each word, checking if its consonant count matches the required number `n`, if so, it adds the word to the `result` list. 

Here is a sample output of the function:
```
select_words("Mary had a little lamb", 4) ==> ["little"]
select_words("Mary had a little lamb", 3) ==> ["Mary", "lamb"]
select_words("simple white space", 2) ==> []
select_words("Hello world", 4) ==> ["world"]
select_words("Uncle sam", 3) ==> ["Uncle"]
```

This problem can be solved in different ways, this solution uses a counting consonants technique. Another approach could be to use regex patterns to identify patterns in the string that match desired counts. 

Note: this code assumes that the input string contains only letters and spaces. 
If the input may contain other characters, additional handling would be necessary.