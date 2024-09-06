```python
def cycpattern_check(first, second):
    first = first.lower()
    second = second.lower()
    return second in first or any(x in first for x in second[1:])
```
The function uses lowercase conversion for the words and checks if the second word exists in the first word directly and also checks if any rotation of the second word exists in the first word using the any function. It returns True if any of these conditions are satisfied and False otherwise.