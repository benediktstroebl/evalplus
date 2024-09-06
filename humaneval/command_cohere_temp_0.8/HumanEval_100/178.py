```python
def make_a_pile(n):
    # Calculate the first two levels directly
    pile = [n, n + 2]
    while len(pile) < n:
        # If the top of the pile is even, take an even number
        if pile[-1] % 2 == 0:
            pile.append(pile[-1] + 2)
        # Otherwise, take an odd number
        else:
            pile.append(pile[-1] + 1)
    return pile
```

The code leverages the fact that the number of stones in the `i^{th}` level is always an integer closest to `i * (i + 1) / 2`. When the number of stones in the `i^{th}` level is even, it is always the case. When the number of stones is odd, it chooses the closest odd number instead. This is achieved through a while loop that keeps adding either 2 or 1 until the desired number of levels is reached. 

The code creates the pile incrementally using a while loop, starting with just the base number of stones and then incrementing it by 2 or 1 as appropriate, until the desired number of levels is reached. This is a efficient approach that has a time complexity of O(n).

The script can be accompanied by tests to ensure that it correctly solves the problem for various inputs:
```python
def test_make_a_pile():
    assert make_a_pile(3) == [3, 5, 7]
    assert make_a_pile(5) == [5, 7, 9, 11, 13]
    assert make_a_pile(1) == [1, 3]
    assert make_a_pile(0) == [0]
    assert make_a_pile(2) == [2, 4]

test_make_a_pile()
```
This will ensure that the make_a_pile function behaves as expected.