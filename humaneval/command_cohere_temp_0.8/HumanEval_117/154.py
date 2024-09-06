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
    for word in words:
        ct = count_consonants(word)
        if ct == n:
            res.append(word)
    return res
```

The `count_consonants` helper function takes a word as input and calculates the number of consonants in that word. It checks each character of the word and increments a counter if the character is a consonant. 

The `select_words` function splits the input string into a list of words, and then iterates through each word. For each word, it calls the `count_consonants` function to calculate the number of consonants, if the count matches the required count `n`, the word is added to the result list. 

The script appropriately solves the problem and matches the provided examples.