```python
def count_cons(word):
    con = 0
    for char in word:
        if char != 'a' and char != 'e' and char != 'i' and char != 'o' and char != 'u':
            con += 1
    return con

def select_words(s, n):
    words = s.split()
    result = []
    for word in words:
        con = count_cons(word)
        if con == n:
            result.append(word)
    return result
```
The `count_cons` function counts the number of consonants in a given word, ignoring vowels. The `select_words` function splits the string into words, iterates through each word, and checks if the count of consonants matches the required `n`, including the word in the `result` list if true. The code returns the `result` list of words containing `n` consonants. It addresses the problem's stipulation of returning the list of words in order of appearance in the string `s` while excluding vowels in the counting.