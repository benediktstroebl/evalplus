```python
def will_it_fly(q, w):
    return (len(q) == 1 or q == q[::-1]) and sum(q) <= w
```

The function will return True if the object will fly, and False otherwise. The condition len(q) == 1 or q == q[::-1] checks if the list q is palindrome, q == q[::-1] checks if the list is symmetric on both sides, and the condition sum(q) <= w checks if the sum of the object is less than or equal to the maximum weight. 

Here is a test suite that can be used to test the functionality of the code:
```python
def test_will_it_fly():
    # Test case 1
    q = [1, 2]
    w = 5
    expect = False
    actual = will_it_fly(q, w)
    assert actual == expect, f"For q={q} and w={w}, the function should return {expect}, but it returns {actual}."

    # Test case 2
    q = [3, 2, 3]
    w = 1
    expect = False
    actual = will_it_fly(q, w)
    assert actual == expect, f"For q={q} and w={w}, the function should return {expect}, but it returns {actual}."

    # Test case 3
    q = [3, 2, 3]
    w = 9
    expect = True
    actual = will_it_fly(q, w)
    assert actual == expect, f"For q={q} and w={w}, the function should return {expect}, but it returns {actual}."

    # Test case 4
    q = [3]
    w = 5
    expect = True
    actual = will_it_fly(q, w)
    assert actual == expect, f"For q={q} and w={w}, the function should return {expect}, but it returns {actual}."

test_will_it_fly()
```
The test suite tests the function with different inputs and verifies that the function returns the correct outputs. 

The test suite passes if all the tests pass, and it fails if any of the tests fail. 

You can use this test suite to comprehensively test the solution to the problem and ensure that it behaves as expected. 
This is beneficial to consistently ensure the correctness of your solution as you continue to modify and refine it, which is a best practice in software development. Holding to this approach would be ideal in solving more problems in your coding journey.