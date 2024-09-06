```python
def concatenate(strings: List[str]) -> str:
    return "".join("".join(strings)  # Composes using tuple unpacking and f-strings for the list comprehension
    return "\n".join(strings, sep="")
```