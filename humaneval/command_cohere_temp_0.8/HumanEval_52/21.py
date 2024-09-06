```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all()` function to iterate over each list element `x` and compare it to the threshold `t`. The `all()` function returns `True` if all comparisons are `True` and `False` otherwise, returning the overall conclusion about the list being below the threshold. 

Here is a markdown code block with a unit test expressing the problem statement:
```python
def test_below_threshold():
    # Testing with a list of numbers below the threshold
    assert below_threshold([1, 2, 4, 10], 100) == True

    # Testing with a list of numbers mixed below and above the threshold
    assert below_threshold([1, 20, 4, 10], 5) == False
```
This block contains two test cases that cover a variety of scenarios: a list that is completely below the threshold and a list with values both below and above the threshold to ensure the function behaves correctly in both situations. 

The `assert` statement confirms that the function returns the expected outcome, allowing for a thorough evaluation of the function's correctness.  This approach ensures that the function behaves as intended, providing a reliable solution to the problem.