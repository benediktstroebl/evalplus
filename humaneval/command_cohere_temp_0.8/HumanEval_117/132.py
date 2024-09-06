Here's a Python script that defines a function `select_words` to solve the problem:
```python
def select_words(s, n):
    consonants = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'} 
    words = s.split() 
    result = [] 
    for word in words: 
        cnt = 0 
        for c in word: 
            if c in consonants: 
                cnt += 1 
        if cnt == n: 
            result.append(word) 
    return result if result else [] 
# Test cases
print(select_words("Mary had a little lamb", 3))
print(select_words("simple white space", 2))
print(select_words("Hello world", 4))
print(select_words("Uncle sam", 3))
```
This code defines a function that takes a string `s` and an integer `n` as input and returns a list of words from the string that contain exactly `n` consonants. The function is designed to work with strings that contain only letters and spaces.

Here is the code's explanation:
- The consonant dictionary stores all consonants in the English alphabet, with keys as consonants and values as none. This is used to check whether a character is a consonant or not.
- The string `s` is split into a list of words using the `split()` method, which allows us to manipulate each word independently.
- The `result` list is initialized to store words that contain the specified number of consonants. 
- A loop goes through each word in the `words` list. Using a nested loop, each character in the word is checked to see if it is a consonant. The `cnt` variable keeps track of how many consonants are in the word.
- If the `cnt` equals the specified `n`, the word is added to the `result` list. 
- Finally, the function returns a list of selected words. The empty list is returned if there are no qualifying words or an empty input string.

The example usage demonstrates the behavior of the function for different test cases.