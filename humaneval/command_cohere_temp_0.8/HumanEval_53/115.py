```python
def add(x: int, y: int):
    return x + y
```
The function takes in two arguments, x and y, both of type integer, and it returns the sum of the two values. 

To pass tests, you can create a Markdown file with the corresponding test code blocks. For example, you can create a file called `tests.md` with the following content:
```python
>>add(2, 3)
5
>>add(5, 7)
12
```

If you execute this test file with the `add` function in a Python environment that supports Markdown, the tests should pass. 
For example, you can use this command in your terminal:
```bash
python -m markdownlint --strict --quiet tests.md
``` 
If the tests pass, the program will not give you any feedback, and you can safely assume that the tests passed. If they are incorrect, error messages will be displayed. 
This way, the `add` function is tested and validated to produce the expected behavior.  You can easily adapt this method to test other functions and validate their behavior regarding given inputs and expected outputs.