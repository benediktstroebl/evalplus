```python
def count_consonants(word):
    """Count consonants in a word"""
    word = word.lower()
    total = 0
    for char in word:
        if char in "bcdfghjklmnpqrstvwxyz":
            total += 1
    return total

def select_words(s, n):
    """Return list of words containing exactly n consonants"""
    words = s.split()
    result = []
    for word in words:
        consonant_count = count_consonants(word)
        if consonant_count == n:
            result.append(word)
    return result
```
The `count_consonants` function is used to calculate how many consonants there are in a given word. This is important for this problem because it allows us to determine whether a word contains exactly n consonants. The `select_words` function acts as the main driver of this solution, it splits the space into individual words and then uses the above function to determine if each word contains exactly n consonants, if so, it is added to the result list. 

This solution adheres to the problem guidelines as it:
- Determines the consonant count only once for each word during its first encounter (optimization)
- Returns an empty list if the input string is empty.
- Excludes punctuation and spaces from the counting
- Handles various word types and letter cases.

Here is some sample output demonstrating its usefulness:
```
> select_words("Mary had a little lamb", 3) ==> ["Mary", "lamb"]
```
```
> select_words("simple white space", 2) ==> []
```
```
> select_words("Hello world", 4) ==> ["world"]
```
```
> select_words("Uncle sam", 3) ==> ["Uncle"]
```