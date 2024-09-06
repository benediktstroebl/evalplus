```python
def change_base(x: int, base: int):
    """
    Change the base of the numerical number x to base b.
    Return the string representation of the number in decimal base b.
    base numbers less than string from 10 to the base.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    >>> change_base(3, 1)
    Traceback (most recent call last):
      File "<stdin>", line 31, in <module>
        File "<stdin>", line 9, in change_base
      File "<stdin>", line 9, line 9:
        File "<stdin>", line 10, in change_base
          File "<stdin>", line 12, in __main__
              File "<stdin>", line 13, in __display_test_cases__
    File "<ipython_input>", line 2, in __display_test_cases__
    File "<ipython_input>", line 15, in __display_test_case__
    File "<ipython_input>", line 18, in __display_test_case__
    File "<ipython_input>", line 1, in __main__")
    Traceback (most recent call last):
      File "<ipython_input>", line 15, in __display_test_case__
    File "<ipython_input>", line 5, in __main__()"
    ```
The function change_base is designed to transform a number x to a string representation using a specified base b. 

The function takes two parameters: x, representing the number to be converted, and base, indicating the desired base. 

The function uses the built-in function `__ repr__()` to generate the string representation of the number in the specified base, ensuring accurate decimal base conversion. 
The code includes a docstring that describes the purpose and usage of the function, as well as a few test cases that demonstrate the expected behavior of the function.