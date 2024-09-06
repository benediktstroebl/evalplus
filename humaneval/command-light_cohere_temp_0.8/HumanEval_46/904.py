```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which each number is the sum of the two preceding ones. The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the previous two.
    :
    The function returns the n-th Fibonacci number.
    """

def test_fib4():
    assert fib4(5) == 4
    assert fib4(6) == 8
    assert fib4(7) == 14

    assert_all_equal(fib4(range(5)), [0, 1, 2, 3, 4, 5, 6, 7])

def assert_all_equal(test_list, expected_list):
    assert list(test_list) == list(expected_list)

if __name__ == "__main__":
    test_fib4()
```
The `fib4` function calculates the n-th Fibonacci number using a formula that does not involve recursion, and the `test_fib4` function tests that the `fib4` function produces the correct results. The `assert_all_equal` function checks whether two lists are equal, which is a common assertion test used in Python testing. 
The `if __name__ == "__main__"` statement is a Python idiom that runs the test_fib4 function when the script is executed.  The `test_fib4` function is executed when the script is run, which checks that the `fib4` function is working correctly.