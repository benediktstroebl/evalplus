Here's a Python script that contains a function to solve the problem as stated in the code block:
```python
def select_words(s, n):
    consonants = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'}
    words = s.split()
    result = []
    for word in words:
        cnt = 0
        for char in word:
            if char in consonants and char != ' ':
                cnt += 1
        if cnt == n:
            result.append(word)
    return result if result else ['']
```
This approach splits the input string s into a list of words, then loops through each word, counting the number of consonants, and adding the word to the result list if the consonant count matches the required count n. Note that the empty list result is handled by returning a list with at least one empty string, which is the default output for the function if the input string is empty, as stated in the problem statement.