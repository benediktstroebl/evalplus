Here is a self-contained Python script that defines a function that creates a pile of stones with the described structure:
```python
def make_a_pile(n):
    """
    Given a positive integer n, you have to make a pile of n levels of stones. The number of stones in the next level is:
        - the next odd number if n is odd
        - the next even number if n is even
        - starting from 1

    Return: list of stones in each level, where element at index i represents the number of stones in the level (i+1)
    """
    result = []
    for i in range(n+1):
        if n % 2 == 0:
            result.append(next_even)
        else:
            result.append(next_odd)
        next_even = 1
        next_odd = 1
        result.append(next_odd)
        next_even += 2

    return result

def test_make_a_pile():
    """
    >>> test_make_a_pile()
    [1, 3, 5, 7]
    """
    return make_a_pile(4) == [1, 3, 5, 7]
```

The `make_a_pile` function takes an integer n as input and returns a list of stones in each level. The function uses a odd and even numbers to create the pile, starting from 1 and incrementing by 1 until it reaches the desired number.

The `test_make_a_pile` function tests the `make_a_pile` function with the argument 4 and compares the result with the expected output `[1, 3, 5, 7]`.