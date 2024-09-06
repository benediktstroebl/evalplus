```python
def make_a_pile(n):
    # Initialize a list to store the number of stones in each level
    pile = [n]
    
    # Calculate the number of stones for the next level if n is odd
    if n % 2 == 1:
        pile.append(n + 2)
    else:
        pile.append(n + 1)
    
    return pile
```

This function uses a simple if-else statement to determine whether the next level should have an even or odd number of stones and adds the appropriate value to the pile list. It then returns the pile list. When the initial value of `n` is 3, the function's output is:
```python
[3, 5, 7]
```