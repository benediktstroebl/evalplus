```python
def make_a_pile(n):
    pile = [n]
    while len(pile) < n+1:
        if n % 2 == 1:
            n += 2
        else:
            n += 1
        pile.append(n)
    return pile
```
This function uses a simple loop to create the pile, where each iteration adds the next even number to the pile if the previous number was odd, and vice versa. The loop continues until the pile has `n+1` numbers, so it must be the base case where `n == 1` unless the pile cannot grow anymore. The resulting list is then returned.

Here is a markdown code block containing a test case that validates the solution:
```python
def test_make_a_pile():
    assert make_a_pile(3) == [3, 5, 7]
```

The 3 in the test case represents the number of stones in the first level, so the expected output is [3, 5, 7], meaning 3 stones in the first level, 5 in the second, and 7 in the third. The `assert` statement checks whether the output of the function is equal to the expected output and throws an error if they are not equal, ensuring the correctness of the solution.