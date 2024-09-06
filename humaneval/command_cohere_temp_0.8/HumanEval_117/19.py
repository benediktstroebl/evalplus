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
        if count_cons(word) == n:
            words.append(word)
    return words if words != [] else words

# Test Cases
print(select_words("Mary had a little lamb", 3))
print(select_words("simple white space", 2))
print(select_words("Hello world", 4))
print(select_words("Uncle sam", 3))
``` 

This Python script solves the problem using a two-step approach:
1. First, we define a helper function `count_cons` that calculates the number of consonants in a given word. This function helps us avoid repeated calculations of consonants in different words.
2. Next, the `select_words` function takes the input string `s` and counts `n` and uses `count_cons` to filter words accordingly. It then returns a list of words that contain exactly `n` consonants.

The provided test cases help validate the script's behavior and ensure that it handles various scenarios correctly. Adjust the test cases to cover more edge scenarios if needed.  This approach ensures efficiency and readability.