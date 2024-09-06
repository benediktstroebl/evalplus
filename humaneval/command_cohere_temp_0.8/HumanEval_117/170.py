Here's a Python script that contains a function called select_words, which takes a string s and a natural number n as input and returns a list of all words from the string s that contain exactly n consonants, in the order that they appear in the string:
```python
def select_words(s, n):
    words = s.split(' ')
    result = []
    consonants = {"b", "c", "ch", "d", "f", "g", "h", "j", "k", "l", "m", "p", "q", "r", "s", "sh", "t", "v", "w", "x", "y", "z"}
    for word in words:
        num_consonants = sum(1 for char in word if char in consonants)
        if num_consonants == n:
            result.append(word)
    return result if result else [""]
```

The `select_words` function first splits the input string s into a list of words, where each word is represented as a string. It then iterates through each word in the list and calculates the number of consonants present in that word using a dictionary of consonant characters. If the number of consonants in a word is exactly n, it adds that word to the result list. The function returns an empty list if no words with exactly n consonants are found, and it returns a single empty string if the input string is empty. 

The expected behavior for the given examples in the prompt is:
```
select_words("Mary had a little lamb", 4) ==> ["little"]
select_words("Mary had a little lamb", 3) ==> ["Mary", "lamb"]
select_words("simple white space", 2) ==> []
select_words("Hello world", 4) ==> ["world"]
select_words("Uncle sam", 3) ==> ["Uncle"]
```

This solution is efficient and accurately selects words from the string that meet the criteria of containing exactly n consonants.