```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    n = len(l)
    result = [0] * n
    for i in range(n):
        result[i] = l[i] + 1
    return result
 
def test_incr_list():
    """Function to test the incr_list function"""
    lst = [5, 3, 2, 1]
    expect = [6, 4, 6, 2]
    result = incr_list(lst)
    assert result == expect, "Incorrect result"

def main():
    test_incr_list()

if __name__ == "__main__":
    main()
``` 
This code defines two functions: incr_list and test_incr_list. The incr_list function takes an input list and returns a new list with each element incremented by 1. The test_incr_list function is a simple test function that creates a list with specific values and calls the incr_list function to get the result. Finally, the main function is the entry point for the script and calls the test_incr_list function to run the tests.