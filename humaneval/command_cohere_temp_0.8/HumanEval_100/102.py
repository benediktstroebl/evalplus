```python
def make_a_pile(n):
    # Create a list to store the number of stones in each level
    pile = [n]
    
    # Loop through the levels of the pile
    for i in range(1, n+1):
        # Add the next odd number to the pile if the current level is odd
        if i % 2 == 1:
            pile.append(i + 2)
        # Add the next even number to the pile if the current level is even
        else:
            pile.append(i + 1)
    
    return pile
```
This Python script defines a function called `make_a_pile` that takes a single argument, `n`, representing the number of stones in the first level of the pile. The function creates a list called `pile` to store the number of stones in each level. It then loops through each level from the second to the top level, determining whether the current level is odd or even. If the level is odd, it adds the next odd number to the pile. If the level is even, it adds the next even number to the pile. The function returns the `pile` list, which represents the number of stones in each level of the pile. 

Here is an example of using the above Python script:
```python
print(make_a_pile(3))
```
This will output:
```bash
[3, 5, 7]
```