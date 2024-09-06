```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

#Test cases
test_max_element = [
    lst=[1, 2, 3],
    assert max_element(lst) == 3, "max element not found"
   
  ]

# main function test
test_max_element_main = test_max_element

if __name__ == "__main__":
    # run the test suite
    unittest.run(test_max_element_main)
``` 
This code defines a function max_element that calculates the maximum element in a given list. The function uses the max() function from the built-ins to find the maximum value in the list. 

The code also has a test suite that checks whether the max_element function correctly finds the maximum element in the given list. 

Finally, the script runs the test suite using the unittest.run() function to verify that the function works as expected.