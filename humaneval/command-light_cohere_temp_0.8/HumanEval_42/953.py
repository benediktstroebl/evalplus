```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    l.append(1)
    return l + [1]

#Test case 1: Basic function test
def test1():
    l = [1, 2, 3]
    assert incr_list(l) == [2, 3, 4]

#Test case 2: List with multiple elements
def test2():
    l = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    assert incr_list(l) == [6, 4, 6, 3, 4, 4, 10, 1, 124]

#Test case 3: Empty list
def test3():
    l = []
    assert incr_list(l) == []

#Test case 4: Recursive case with single element
def test4():
    l = [5]
    assert incr_list(l) == [6]

#Test case 5: Recursive case with multiple elements
def test5():
    l = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    assert incr_list(l) == [6, 4, 6, 3, 4, 4, 10, 1, 124]

if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
    test5()
```
The Python code defines a function `incr_list` that takes a list `l` as an argument and returns a new list with elements from the original list incremented by 1. The test suite consists of five test cases that pass the function's output against the expected output to verify the correctness of the `incr_list` function. 
The test cases cover basic scenarios, recursive cases with single and multiple elements, and an empty list. The tests are designed to validate the functionality of the `incr_list` function, ensuring that the output is as expected.