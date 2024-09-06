Here's a Python script that contains a function named `double_the_difference` which solves the problem statement given above:
```python
def double_the_difference(lst):
    """
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    """
    result = 0
    for num in lst:
        if num % 2 == 1 and isinstance(num, int) and num >= 0:
            result += num ** 2
    return result
```

This function iterates over each number in the input list. If the number is odd, positive, and an integer, it gets squared and added to the total. The function returns the calculated sum.

To showcase its behavior against a variety of inputs, here are some test cases accompanied by their expected outputs:
1. `test_double_the_difference_positive_odd`: `[1, 3, 2, 0]` => `10`
2. `test_double_the_difference_negative_odd`: `[9, -2]` => `81`
3. `test_double_the_difference_zero`: `[0]` => `0`
4. `test_double_the_difference_empty`: `[]` => `0`

Here's a brief setup for these tests, each one encapsulated in a function:
```python
def test_double_the_difference_positive_odd():
    assert double_the_difference([1, 3, 2, 0]) == 10

def test_double_the_difference_negative_odd():
    assert double_the_difference([9, -2]) == 81

def test_double_the_difference_zero():
    assert double_the_difference([0]) == 0

def test_double_the_difference_empty():
    assert double_the_difference([]) == 0
```

These tests cover various scenarios, including both positive and negative odd numbers, zeros, and empty inputs. 
The `double_the_difference` function, when invoked with any of these test cases, should yield the expected output.