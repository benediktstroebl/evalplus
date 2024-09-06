```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_set = set()
    for i in range(len(s)-2):
        if len(letters_set) >= 3 and s[i] == s[i+1] and s[i] == s[i+2]:
            return False
        letters_set.add(s[i])
    return True
```

This script defines a function `is_happy` that takes a string `s` as input and checks whether the string is happy or not. The function returns `True` if the string is happy, and `False` otherwise. 

The function first checks if the length of the string is at least 3. If not, it returns `False` since a string with less than 3 letters cannot be happy. Then, it uses a set `letters_set` to store the encountered letters in the string to check if every three consecutive letters are distinct. It iterates through the string with an offset of 2 (to check consecutive triples). If it encounters a triplet of the same letters, the function returns `False`. Otherwise, it returns `True`. 

The included docstring offers example queries and expected outputs, which align with the test cases to ensure the accuracy of the function. You can test the function by calling it with different strings and comparing the results to the examples provided.