```python
def add(x: int, y: int):
    return x + y
```
```python
import pytest

@pytest.mark.parametrize('input, expected', [
    (2, 3, 5),
    (5, 7, 12)
])
def test_add(input, expected, markdown):
    actual = add(input, input + expected)
    assert actual == expected
    markdown.append('```python\nadd({input}, {input + expected}) == {expected}\n```'.format(
        input=input,
        expected=expected
    ))
```
The function `add` takes two integers as inputs and returns their sum. 

Then, the `test_add` function verifies that the `add` function correctly computes the sum of two integers. It uses the `pytest.mark.parametrize` decorator to create test cases from `input`, `expected`, and the expected output of the function. The actual output of the function is stored in `actual`, and `markdown` is used to store the test code block. 

To run the test cases, you can copy the script into a Python file (e.g., `test_add.py`) and execute the file. 

Note: The `markdown` variable is a fixture provided by `pytest-markdown` that allows you to create markdown content as part of your tests. After the tests run, the resulting markdown content is printed to the console. If you prefer to have the content in a separate markdown file, you can change the fixture resolution by adjusting your `pytest` configuration in the file `pytest.ini` or by using the command line flag `--fixture-arg`.