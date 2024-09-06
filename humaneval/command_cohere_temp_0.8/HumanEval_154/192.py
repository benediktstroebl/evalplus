```python
def cycpattern_check(first, second):
    first = first.lower()
    second = second.lower()
    return second in first or any(second in s for s in first.split(second))
```
This function takes two words as input and evaluates whether the second word or any of its rotations are a substring in the first word. The function first converts the input to lowercase to ensure case-insensitive matching. It then checks if the second word is directly present in the first word. Additionally, it iterates through the individual characters of the first word, checking if the second word, or any rotation of it, is a substring in those characters. The function returns True if any of these conditions are met, indicating the presence of a cyclic pattern.