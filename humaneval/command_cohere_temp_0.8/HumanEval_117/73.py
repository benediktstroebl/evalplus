```python
def count_consonants(word):
    cnt = 0
    for char in word:
        if char.isalpha():
            if char.lower() != 'a' and char.lower() != 'e' and char.lower() != 'i' and char.lower() != 'o' and char.lower() != 'u':
                cnt += 1
    return cnt

def select_words(s, n):
    words = s.split()
    result = []
    for word in words:
        if count_consonants(word) == n:
            result.append(word)
    return result
```
The provided Python script implements the `select_words` function, which takes a string `s` and an integer `n` as inputs. This function returns a list of all words from the string `s` that contain exactly `n` consonants.

The `count_consonants` function is also included, which calculates the number of consonants in a given word. It iterates through each character in the word and checks if it is an alphabet character. If so, it determines whether the character is a vowel or not. If it's not a vowel, it counts it as a consonant; otherwise, it skips ameliorating the count, which is initialized at 0. The word is then checked to see if it has the desired number of consonants.

The `select_words` function first splits the input string `s` into a list of words. It then iterates through each word, checking if it contains exactly `n` consonants using the `count_consonants` function. If a word has the desired number of consonants, it is added to the `result` list. Finally, the function returns the `result` list containing the selected words.

The script passes example test cases provided in the original statement, including "select_words("Mary had a little lamb", 4) ==> ["little"]", "select_words("Mary had a little lamb", 3) ==> ["Mary", "lamb"]", "select_words("simple white space", 2) ==> []", and "select_words("Hello world", 4) ==> ["world"]".

Thus, this code provides an accurate solution to the problem, satisfying the throwaway requirement of a self-contained script.