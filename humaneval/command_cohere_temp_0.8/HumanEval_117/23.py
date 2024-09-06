Here's a Python script that contains a function called select_words, which takes a string s and a natural number n as input and returns a list of all words from the string s that contain exactly n consonants:
```python
def select_words(s, n):
    ls = []
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    word = ""
    for c in s:
        if c == " ":
            if len(word) == 0:
                continue
            elif len(word) == 1:
                ls.append(word)
            else:
                word = ""
        elif c in consonants:
            word = word + c
        else:
            if len(word) == n:
                ls.append(word)
                word = ""
    if len(word) == n:
        ls.append(word)
    return ls
```
This Python script defines a function **select_words** that takes a string s and an integer n as inputs. It aims to find words in the string that contain exactly n consonants. The script uses a list ls to store these words and a consonant string to identify consonants. It iterates through the input string, adding characters to the current word if they are consonants. When a space is encountered, the function checks the length of the current word. If it's of length 1 or greater, it's added to ls or reset if it's empty. If the current word has exactly n consonants, it's added to the list and reset. Finally, the last word is checked, and if it contains exactly n consonants, it's added to ls. The result is a list of words with exactly n consonants.