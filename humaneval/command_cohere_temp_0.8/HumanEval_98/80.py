```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    upside_vowels = {'A':1, 'E':1, 'I':1, 'O':1, 'U':1}
    return sum(1 for i, char in enumerate(s) if char.isupper() and upside_vowels.get(char, 0) and i%2 == 0)
```
The function uses a dictionary to map each uppercase vowel to a value of 1, and then uses a generator expression along with the `enumerate` function to check if the character is a vowel and whether its index is even. The sum function then adds up the number of uppercase vowels in even indices and returns the total. This solution is efficient and well-organized.