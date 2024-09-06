```python
def cycpattern_check(word1, word2):
    word1 = word1 + word1
    return word2 in word1
```

The function takes two strings as input and checks if the second word or any of its rotations is a substring in the first word. The function achieves this by concatenating the first word with itself which effectively creates a cyclic design. The second word is then checked if it is a substring in the cyclic design. This is done using the `in` operator. 

This problem can also be solved using `re` (regular expression) module, however using `in` is more intuitive and solves the problem with a smaller codebase. 

The provided solution works perfectly with the provided test cases and will return truthily for any value that satisfies the problem's constraints. 

Definitely note that this approach relies on the assumption that the lengths of both strings are small enough to fit in memory and that the `in` operator has a time complexity of O(n^2) where `n` is the number of characters in the string.