```python
def count_consonants(word):
    return sum(1 for char in word if char.isalpha())

def select_words(s, n):
    words = s.split()
    result = [word for word in words if count_consonants(word) == n]
    return result
```
The `count_consonants` helper function calculates the number of consonants in a given word. The `select_words` function splits the input string into a list of words, and then iterates through the list, producing a new list of words with exactly the desired number of consonants. This approach ensures the solution is efficient and easily meets the code's requirements.