Here's a Python script that contains a function eat() that solves the problem described in the markdown code block:
```python
def eat(n, need, rem):
    return [n + need, max(0, rem - need)]
```
This function takes in three variables: num, need, and remaining. It attempts to eat more if there are remaining carrots, or it will just return the total eaten and display 0 for remaining as you will still be hungry even though there are no more carrots left to eat. This function returns a list of the total carrots eaten after meals and the number of carrots left after meals. 

This approach takes into account the constrains mentioned with the following code:
```python
# Constrains
assert 0 <= n <= 1000, "n should be less or equal to 1000"
assert 0 <= need <= 1000, "need should be less or equal to 1000"
assert 0 <= rem <= 1000, "remaining should be less or equal to 1000"
```
This way the function eats the correct amount based on the input provided.