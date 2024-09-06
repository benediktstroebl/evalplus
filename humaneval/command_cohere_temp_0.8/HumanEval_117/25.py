```python
def count_consonants(word):
    return sum(1 for char in word if char in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")

def select_words(s, n):
    words = [word for word in s.split() if word]
    return [word for word in words if count_consonants(word) == n]
```
The `count_consonants` helper function calculates the number of consonants in a given word, providing a reliable metric for assessing conformity to the requested count. The `select_words` function then segregates the input string into individual words and assesses each word's consonant count. If the word contains precisely n consonants, it is included in the final list. This method guarantees that only words with the desired number of consonants are chosen from the input string. 

This approach, which consists of breaking down the problem into smaller parts, allows for more manageable code and assists in maintaining a clear understanding of the total problem. Furthermore, it has the potential to be more efficient because each function has a single responsibility, making it easier to test and debug.