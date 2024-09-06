```python
def count_cons(word):
    ct = 0
    for char in word:
        if char != 'a' and char != 'e' and char != 'i' and char != 'o' and char != 'u':
            ct += 1
    return ct
    
def select_words(s, n):
    words = []
    str_list = s.split()
    for word in str_list:
        ct = count_cons(word)
        if ct == n:
            words.append(word)
    return words
```
The main algorithm splits the string s into a list of words (tokens) and then loops through each word, counting the number of consonants in each word using the `count_cons` helper function. If the word contains exactly n consonants, it is added to the words list, which accumulates the solution. The algorithm then returns the list of words that contain exactly n consonants. 

The `count_cons` helper function counts the number of consonants in a given word. It iterates through each character in the word and checks if the character is a consonant or not. The character is considered a consonant if it is not one of the vowels 'a', 'e', 'i', 'o', or 'u'. If the character is a consonant, it increments a counter that tracks the total number of consonants in the word. Finally, the function returns the count of consonants in the word. 

Overall, the code efficiently solves the problem in a self-contained manner, achieving a linear time complexity of O(n + m), where n is the number of words and m is the maximum length of a word in the input string.