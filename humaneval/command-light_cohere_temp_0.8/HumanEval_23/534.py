Here's a self-contained Python script with a function `strlen` that calculates the length of a given string:
```python
def strlen(string: str) -> int:
    return len(string)

# Testing the function
>>> strlen('')
0
>>> strlen('abc')
3
>>> strlen('')anche')
Traceback (most recent call last):
  File "<input>", line 3, in <module>
SyntaxError: invalid syntax 
   [...]
```