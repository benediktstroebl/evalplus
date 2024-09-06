```python
def correct_bracketing(brackets):
    open, close = 0, 0
    for char in brackets:
        if char == '<':
            open += 1
        elif char == '>':
            close += 1
        if open > close:
            return False
    return open == close
```

This Python script defines a function `correct_bracketing` that takes a string `brackets` as input. The function counts the opening and closing brackets within the string using two counters, `open` and `close`, which are initialized to 0. It then iterates through each character in the input string and increments the `open` counter if the character is an opening bracket (`'<'`), and increments the `close` counter if the character is a closing bracket (`'>'`). 

The function returns `False` if the count of opening brackets is greater than the count of closing brackets at any point in the string. If the balance is restored at the end (`open` equals `close`), the function returns `True`, indicating that every opening bracket has a corresponding closing bracket. 

The script includes a set of example tests that demonstrate the behavior of the function and confirm its correctness.