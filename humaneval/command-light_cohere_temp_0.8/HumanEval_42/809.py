```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    return [i+1 for i in l]

# Test function
def test_incr_list():
    """Test the incr_list function."""
    assert incr_list([1, 2, 3]) == [2, 3, 4]
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
    assert incr_list([]) == []
    assert incr_list([10, 20, 30]) == [10, 20, 30]

# Main function
def main():
    print("Result of incr_list function: ", end="")
    print(incr_list([1, 2, 3]))

# Run the test and the main functions
test_incr_list()
main()
``` 
The function incr_list takes a list l as input and returns a new list with elements incremented by 1. The test_incr_list function tests the incr_list function with various inputs and ensures the function is working correctly. The main function then prints the result of the incr_list function and runs the test_incr_list function.