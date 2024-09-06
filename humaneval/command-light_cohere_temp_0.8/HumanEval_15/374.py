```python
def string_sequence(n: int) -> str:
    return f" {0:0b}  {1:0b}  {2:0b}  {3:0b}  {4:0b}  {5:0b}"
    for i in range(n+1):
        yield i ,  str(i)

def test_string_sequence():
    n = 5
    assert string_sequence(n) == '0 5 10 15 20'
```
The function 'string_sequence' takes an integer n as input and returns a string containing space-separated numbers from 0 to n. The function utilizes a 'yield' statement to iterate over the numbers from 0 to n, and each yield statement creates a tuple with the current number and its string representation. The 'test_string_sequence' function tests whether the string sequence function produces the correct output for the given value of n = 5.