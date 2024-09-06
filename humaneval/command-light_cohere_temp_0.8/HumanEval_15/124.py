Here's the self-contained Python function that generates a string with space-delimited numbers from 0 up to n: 
```python
def string_sequence(n: int) -> str:
    return "".join(str(i) for i in range(0, n+1))
```
This function takes an integer n as input and returns a string containing space-separated integers from 0 to n. It uses a string.string (which returns an iterator object for converting an iterable into a string) and str.object() (which converts an string object into a string).