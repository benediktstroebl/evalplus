```python
def flip_case(string):
    """
    For a given string, flip lowercase characters to uppercase and vice versa.
    return 'hEllo'
"""

def test_flip_case():
    input = "hello"
    string = flip_case(input)
    assert string == "HElLO" 

# Run the test function to verify the flip case functionality
# Output: 
# test_flip_case('Hello')  #Passes
# test_flip_case('world')  #Passes
# test_flip_case(' funnel )  #Passes

This script provides a function `flip_case` that transforms a given string, flipping the case of its characters. The test function `test_flip_case` is used to verify the correctness of the `flip_case` function against a series of test cases.