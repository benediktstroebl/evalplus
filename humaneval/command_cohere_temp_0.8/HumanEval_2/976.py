```python
def truncate_number(number: float) -> float:
    return number - int(number)
```

The code uses an intuitive approach that subtracts the integer part of the number from the total number, eventually returning the leftover fractionary part as requested. This is underpinned by the mathematical property that subtracting an integer from a number does not modify its fractional part. 

This approach is elegant in its simplicity, providing a straightforward solution to the problem. It is important to note, however, that this approach assumes the input is a valid numerical value, and does not handle edge cases such as inputs being NaN or Infinity.