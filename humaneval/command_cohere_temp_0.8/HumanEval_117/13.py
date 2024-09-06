```python
def count_consonants(word):
    return sum(1 for char in word if char in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")

def select_words(s, n):
    words = s.split()
    result = [word for word in words if count_consonants(word) == n]
    return result
```
The provided Python script implements the `select_words` function as per the problem statement. It first splits the input string `s` into individual words using spaces as separators. For each word, it counts the number of consonants using a generator expression. Generator expressions are used to iterate over each character in a word and check if each character is a consonant. The count of consonants for each word is then compared to the target number `n`. If the count is equal to `n`, the word is added to the `result` list. Finally, the function returns the `result` list, which contains all words from the input string with exactly `n` consonants. 

This solution uses a generator expression, which can be more memory-efficient for large inputs compared to a list comprehension. Also, the function `count_consonants` is reused for counting consonants in each word, ensuring simplicity and efficiency. The solution handles various test cases as specified in the problem statement, including edge cases with empty strings or uncommon target numbers.