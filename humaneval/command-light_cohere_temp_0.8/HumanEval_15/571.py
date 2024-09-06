```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n + 1)
    ```
The above code generates a string that contains space-separated numbers from 0 up to n, including n. The function uses the string formatting with f-string expansion and the technique of creating a new string by concatenating strings together with the provided value for n.