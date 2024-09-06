```python
def count_cons(word):
    cons = 0
    for char in word:
        if char != 'a' and char != 'e' and char != 'i' and char != 'o' and char != 'u':
            cons += 1
    return cons

def select_words(s, n):
    words = s.split()
    result = []
    for word in words:
        cons = count_cons(word)
        if cons == n:
            result.append(word)
    return result
```

The code defines a helper function `count_cons` that calculates the number of consonants in a given word. The main function `select_words` splits the string into a list of words, then iterates through each word, calculates its consontants, and adds it to a list if it has exactly n consonants. The code assumes the input string only contains letters and spaces. 

The code would work as expected for the test cases provided. For example, it would return `["little"]` for the input `"Mary had a little lamb"` and `["Mary", "lamb"]` for the input `"Mary had a little lamb"` with n = 3.