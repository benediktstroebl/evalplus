```python
def count_cons(word):
    con = 0
    for char in word:
        if char != 'a' and char != 'e' and char != 'i' and char != 'o' and char != 'u':
            con += 1
    return con

def select_words(s, n):
    words = []
    str_list = s.split()
    for word in str_list:
        con = count_cons(word)
        if con == n:
            words.append(word)
    return words
```
The provided Python script aims to solve a particular problem: finding all words in a given string that contain exactly a certain number of consonants. To achieve this, it defines two functions. The first function, `count_cons`, calculates the number of consonants in a given word. It iterates through each character in the word and checks if the character is a consonant, excluding the vowels 'a', 'e', 'i', 'o', and 'u'. The second function, `select_words`, takes an input string `s` and a target number of consonants `n`. It splits the input string into a list of words and then iterates through each word, calling `count_cons` to count the consonants. If a word contains exactly `n` consonants, it's added to the `words` list. 

This code will return the list of words containing exactly n consonants if such words exist in the string. However, it's worth noting that this code assumes the input string contains only letters and spaces, and may need additional checks for other characters. Also, it could benefit from optimizations like checking the length of words before counting consonants, especially if handling large strings.