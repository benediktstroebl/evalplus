Here's a Python script that contains a function called select_words, which takes a string s and a natural number n as input and returns a list of all words from the string that contain exactly n consonants:
```python
def select_words(s, n):
    words = s.split(' ')
    result = []
    for word in words:
        ct = 0
        for c in word:
            if c != ' ':
                ct += 1
        if ct == n or (n == 0 and ct == 0):
            result.append(word)
    return result
```

The script first splits the string into a list of words. Then, it iterates through each word, counting the number of consonants (i.e., letters that are not spaces). If the count of consonants is equal to the target number n, or if n is zero and the word is all spaces, it adds the word to the result list. Finally, the function returns the list of words that meet the criteria. 

This solution is straightforward and efficiently selects the words containing the desired number of consonants, order being preserved from the given string. And if the string contains only spaces or none, it returns an empty list respectively, as per the problem statement.