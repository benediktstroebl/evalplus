```python
def count_cons(word):
    ct = 0
    for char in word:
        if char != 'a' and char != 'e' and char != 'i' and char != 'o' and char != 'u':
            ct += 1
    return ct
    
def select_words(s, n):
    words = []
    for w in s.split():
        ct = count_cons(w)
        if ct == n:
            words.append(w)
    return words

# Example usage
print(select_words("Mary had a little lamb", 4))
```

This code contains two functions: 

1. The `count_cons` function counts the number of consonants in a given word. It loops through each character in the word and checks if the character is a consonant, incrementing a consonant counter if it is. 

2. The `select_words` function accepts a string `s` and an integer `n` as input and returns a list of all words that contain exactly `n` consonants. It iterates through each space-separated word in the string, calculates the number of consonants using the `count_cons` function, and adds the word to the list if the consonant count matches the desired count `n`.

In the example provided in the code, it passes the test case `select_words("Mary had a little lamb", 4)` which returns `["little"]`.