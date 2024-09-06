```python
def count_consonants(word):
    ct = 0
    for char in word:
        if char != 'a' and char != 'e' and char != 'i' and char != 'o' and char != 'u' and \
           char != 'A' and char != 'E' and char != 'I' and char != 'O' and char != 'U' and \
           char != 'y' and char != 'Y':
            ct += 1
    return ct
    

def select_words(s, n):
    words = s.split()
    res = []
    for w in words:
        ct = count_consonants(w)
        if ct == n:
            res.append(w)
    return res
```

The primary function `select_words` takes two parameters, a string `s` and an integer `n`. It splits the input string into words and iterates through them. For each word, it calls the helper function `count_consonants` to count the number of consonants in that word and compares it with the target number `n`. If the count matches, the word is appended to the result list. Finally, the function returns the list of words that contain exactly `n` consonants. 

The code assumes that the input contains only letters and spaces, as stated in the problem statement.