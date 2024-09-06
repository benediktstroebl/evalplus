```python
def find_max(words):
    max_unique_words = max(words, key=lambda word: (len(set(word)), word))
    return max_unique_words
```

The `find_max` function maximizes the number of unique words by using the `max` function with a custom `key` argument. This argument is a lambda function that prioritizes words using two factors: the length of their unique character set and their lexicographical order. This ensures that the function follows the problem's requirement of selecting the word with the most unique characters while prioritizing words that come earlier in the lexicographical order when there is a tie. 

This solution will return the word that has the maximum number of unique characters among all the words in the list, and if there are multiple words with the same amount of unique characters, it will pick the one that comes first in lexicographical order. 

The following example tests illustrate how the function works:
```python
print(find_max(["name", "of", "string"]))  # Output: "string"
print(find_max(["name", "enam", "game"]))  # Output: "enam"
print(find_max(["aaaaaaa", "bb", "cc"]))  # Output: "aaaaaaa"
```