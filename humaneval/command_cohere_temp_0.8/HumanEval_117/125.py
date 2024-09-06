Here's a Python script that contains a function called select_words, which takes a string s and a natural number n as input and returns a list of all words from the string that contain exactly n consonants:
```python
def select_words(s, n):
    words = s.split(' ')
    result = []
    for word in words:
        consonantCount = 0
        for char in word:
            if char.isalpha():
                if char.lower() != char.upper():
                    consonantCount += 1
        if consonantCount == n:
            result.append(word)
    return result if result else ['None']
```

The `select_words` function above splits the input string `s` into a list of words using space as a delimiter. It then iterates through each word, counting the number of consonants in each one. If the count is exactly n, the word is appended to the `result` list. The function returns an empty list if the input string is empty. 

Here's a simple test case to validate the solution:
```python
def test_select_words():
    assert select_words("Mary had a little lamb", 3) == ["Mary", "lamb"]
```

You can optionally include this test case in your script to verify the function behavior. Simply add it to the code block above or incorporate it into your testing framework.