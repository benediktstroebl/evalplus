Here's a Python script that defines a function `select_words` to solve the problem:
```python
def select_words(s, n):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    words = s.split()
    result = []

    for word in words:
        cnt = sum(1 for char in word if char in consonants)
        if cnt == n:
            result.append(word)

    return result if result else ['']

# Example usage
print(select_words("Mary had a little lamb", 3))
print(select_words("simple white space", 2))
print(select_words("Hello world", 4))
print(select_words("Uncle sam", 3))
```

This script assumes that the input string contains only letters and spaces, which is noted as a assumption in the problem statement as well. The `select_words` function splits the input string into a list of words and then iterates through each word. It counts the number of consonants in each word and compares it to the given value of `n`. If the count is equal, the word is added to the `result` list, which is returned if it's not empty, and an empty list is returned otherwise.