```python
def find_max(words):
    max_uniq = 0
    max_word = None
    for word in words:
        uniq = set(word)
        if len(uniq) > max_uniq:
            max_uniq = len(uniq)
            max_word = word
    return max_word
```

The function `find_max` uses a simple loop to iterate through the list of words. It uses a set data structure to calculate the unique characters in each word. If the number of unique characters is greater than the previous maximum, it updates the maximum count and saves the word. If multiple words have the same maximum number of unique characters, the lexicographical order ensures that the first occurring one is chosen. 

This approach assumes that each word is a string of unique characters, and does not consider cases where a word appears more than once in the list. It is mentioned in the problem statement that the list contains different words, so this assumption is valid. 

The provided solution is efficient with a time complexity of `O(n * alpha(n))`, where n is the length of the input list and alpha is the Ackermann function representing the aggregate alphabetical order of all words in the list. This is because it iterates through the list once, and for each word, calculates its alphabetical order which has a worst-case complexity of O(n).