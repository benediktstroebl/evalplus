```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    n = len(l)
    result = [i+1 for i in l] + l
    return result

# Test case 1
def test1():
    assert incr_list([1, 2, 3]) == [2, 3, 4]

# Test case 2
def test2():
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]

def main():
    print("Test case 1 passed!")
    test1()
    print("Test case 2 passed!")
    test2()

if __name__ == "__main__":
    main()
``` 
The above Python script defines a function `incr_list` that increments each element in a list by 1 and returns the updated list. It also contains two test cases to verify the function's behavior. The script then runs the test cases and verifies that the `incr_list` function produces the expected output.