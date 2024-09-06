```python
def count_consonants(word):
    return sum(1 for char in word if char in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")

def select_words(s, n):
    words = s.split()
    result = [word for word in words if count_consonants(word) == n]
    return result
```
The `count_consonants` helper function calculates the number of consonants in a given word, providing a clean and efficient way to determine the count without complicated regex or unnecessary code. The `select_words` function splits the input string into words and then filters them based on the consonant count, directly providing the answers to the problem as specified in the prompt. 
The resulting code is clean, efficient, and easy to understand, making it a robust solution for this particular task.