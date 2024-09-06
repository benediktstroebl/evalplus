```python
def add(lst):
    even_odd = []
    for i in range(len(lst)):
        if i % 2 == 1 and lst[i] % 2 == 0:
            even_odd.append(lst[i])
    return even_odd
```

This function defines an empty list 'even_odd' that will be used to store the even numbers located at odd indices of the input list. It then iterates through the input list, checking if the index of each element is odd and if the element itself is even. If both conditions are met, the element is added to the 'even_odd' list. Finally, the function returns the 'even_odd' list, which will contain all the even numbers present at odd indices in the input list. 

To ensure the function is correct, it is recommended to test the function with a variety of cases to ensure that it behaves as expected. Below is a minimal test suite with a few test cases to verify the functionality of the function:
```python
def test_add():
    assert add([4, 2, 6, 7]) == [2]
    assert add([1, 3, 5, 7]) == [5]
    assert add([2, 4, 6, 8, 10]) == [6, 10]
    assert add([0, 2, 4, 6]) == [0, 4]
    assert add([7, 5, 3, 1, 9]) == [3, 7]
```

To run the test suite, you can use the 'pytest' library, which allows effortless execution and reporting of test results. If 'pytest' is installed in your environment, you can run the tests by executing the following command in your terminal:
```bash
pytest -v
```

This will run the test suite and display a detailed report on the number of tests passed, failed, or raised errors. If you want to install 'pytest', you can do so using pip: 
```bash
pip install pytest
``` 

This will install the 'pytest' library, and you can then run the test suite as described above.