Here's the self-contained Python function:
```python
def sort_numbers(input_str: str) -> str:
    """
    Input is a string of numbers, valid choices are 'zero', 'one', ... 
    Returns the string with numbers sorted from smallest to largest.
    """
   
    test cases:
    test_string = "three one five"
    expected = "one three five"
    assert sort_numbers(test_string) == expected
```