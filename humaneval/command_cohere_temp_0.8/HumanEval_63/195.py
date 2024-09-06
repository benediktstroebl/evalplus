```python
def fibfib(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
```
This function uses recursive calls to the previous three terms in the sequence to calculate the nth term, following the definition of the FibFib sequence provided in the prompt. 

Here is a simple test suite that verifies the correctness of the function:
```python
def test_fibfib():
    assert fibfib(0) == 0, "0th term is incorrect"
    assert fibfib(1) == 0, "1st term is incorrect"
    assert fibfib(2) == 1, "2nd term is incorrect"
    assert fibfib(5) == 4, "5th term is incorrect"
    assert fibfib(8) == 24, "8th term is incorrect"
```
To test the function, simply run the script, and it will output the test results.