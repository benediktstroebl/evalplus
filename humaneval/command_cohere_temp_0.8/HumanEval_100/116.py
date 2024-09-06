```python
def make_a_pile(n):
    # Initialize a list to store the pile size at each level
    pile = [n]
    
    # Loop to build the pile level by level
    for i in range(1, n.bit_length() + 1):
        # If the current level is odd, the next level has the next odd number of stones
        if i % 2 == 1:
            pile.append(next_odd(pile[i - 1]))
        # If the current level is even, the next level has the next even number of stones
        else:
            pile.append(next_even(pile[i - 1]))
    
    return pile

# Helper function to find the next odd number after a given number
def next_odd(n):
    return n + 2

# Helper function to find the next even number after a given number
def next_even(n):
    return n + 1
```

This script includes three functions:
- `make_a_pile(n)`: This function takes a positive integer `n` as input and returns a list of stone counts at each level of the pile. It follows the problem's specification, creating an ascending sequence of odd or even numbers, depending on the parity of the level index.
- `next_odd(n)`: This helper function calculates the next odd number after a given number `n`. It's used to determine the count of stones for the next odd-numbered level of the pile.
- `next_even(n)`: This helper function calculates the next even number after a given number `n`. It's used to determine the count of stones for the next even-numbered level of the pile.

The code uses bit manipulation to efficiently iterate through the levels of the pile. The `n.bit_length()` expression returns the number of bits needed to represent the number `n` in binary. Increasing this value by 1 corresponds to moving to the next level of the pile.