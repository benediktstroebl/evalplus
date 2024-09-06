```python
def will_it_fly(q, w):
    return (q == q[::-1] and sum(q) <= w)
```

This function will return True if the object q will fly, and False otherwise. The object q will fly if it is balanced (it is a palindromic list) and the sum of its elements is less than or equal the maximum possible weight w. The function works by first comparing the list q to its reversed version q[::-1] to check if it is balanced. If the list is not balanced, the function returns False. If the list is balanced, it proceeds to check if the sum of its elements is less than or equal the maximum possible weight w. If the sum of the elements is greater than the maximum possible weight w, the function returns False. If the conditions are met, the function returns True. 

This problem can be solved using only Python's basic built-in features, and it suits the Pythonic style, which emphasizes readability and simplicity.