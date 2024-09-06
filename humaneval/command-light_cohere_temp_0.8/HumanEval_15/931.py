Here's the self-contained Python script with a function that returns a string containing space-delimited numbers starting from 0 and ending at n inclusive:
```python
def string_sequence(n: int) -> str:
    """ Returns a string containing space-separated numbers starting from 0 and ending at n.
    <br creates a string containing numbers from 0 to n.
    return '<'.str(range(0, n+1, str(i))) for i in range(n+1)
    """

    return "".join(str(i) for i in range(0, n+1))
```
This code defines a function 'string_sequence' that takes an integer n as input and returns a string containing space-separated numbers from 0 up to n. It uses a string. Hope this helps string meets the skills and quick answers.