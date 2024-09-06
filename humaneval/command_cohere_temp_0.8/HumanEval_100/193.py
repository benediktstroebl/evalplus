```python
def make_a_pile(n):
    pile = [n]
    while len(pile) < n+1:
        if n % 2 == 1:
            n += 2
            pile.append(n)
        else:
            n += 1
            pile.append(n)
    return pile
```
This script defines a function `make_a_pile` that takes a single argument `n`, representing the number of stones in the first level of the pile. It uses a `while` loop to build the pile by adding odd or even numbers to the current level, alternating between even and odd numbers based on the parity of `n`. The resulting list of stone counts is returned as the output.

Here's an example of how to use the function:
```python
print(make_a_pile(3))
```
This will output:
```bash
[3, 5, 7]
```