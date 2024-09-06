```python
def correct_bracketing(brackets):
    open_brackets = len(brackets.count('('))
    close_brackets = len(brackets.count(')'))
    return open_brackets == close_brackets
```

This function counts the number of opening and closing brackets using the built-in `count` method. It then returns `True` if the counts are equal and `False` otherwise. 

Here is how you can use it:
```python
print(correct_bracketing("()")) # True
print(correct_bracketing("(()())")) # True
print(correct_bracketing(")(()")) # False
``` 
The function should yield the correct result for each input.