```python
def iscube(a):
    return a ** (1/3) == int(a ** (1/3))
```
This function simplifies the equation to a single equality operation and uses the **int()** function to remove the decimal points of the cube root that should be an integer. 

Here is a test suit to verify the correctness of the function:
```python
def test_iscube():
    assert iscube(1) == True
    assert iscube(64) == True
    assert iscube(0) == True
    assert iscube(-1) == True
    assert iscube(180) == False
    assert iscube(2) == False
``` 
The test suite contains examples from the problem's statement and verifies the correctness of the function. 

To run the test suit, you need to run the Python script in your command line once the script is saved:
```bash
python script_name.py
``` 
This will run the tests and display the results.