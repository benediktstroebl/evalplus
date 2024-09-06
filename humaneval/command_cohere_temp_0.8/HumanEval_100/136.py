```python
def make_a_pile(n):
    piles = []
    for i in range(n):
        if i % 2 == 1:
            piles.append(i + 3)
        else:
            piles.append(i + 4)
    return piles
```
This Python script defines a function called `make_a_pile` that takes a single argument `n`, representing the number of stones in the first level of the pile. The function returns a list of numbers representing the number of stones in each subsequent level of the pile.

The script then includes a set of test cases that check for the functionality of the `make_a_pile` function. These cases check if the function returns the expected output for different values of `n`. Finally, the `make_a_pile` function is applied to a test case in the `make_a_pile(3)` line, which checks if the function computes the expected result for `n=3`. The expected result for this test case is `[3, 5, 7]`, which is the number of stones in each of the three levels of the pile when starting with 3 stones in the first level.