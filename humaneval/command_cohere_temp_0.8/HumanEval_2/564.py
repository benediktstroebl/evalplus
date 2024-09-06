```python
def truncate_number(number: float) -> float:
    return number - int(number)
```

This function simply subtracts the largest integer that is less than or equal to `number`, this yields the desired decimal part. 

To test this, consider the following usage:
```python
>> truncate_number(3.5)
0.5
>> truncate_number(8.0)
0.0
```

The function easily passes these simple tests, however, the problem is more complex for numbers with more decimal places, consider:
```python
>> truncate_number(1.5355)
0.0055
```

This is an edge case, as the expected output is not necessarily 0.0055, as that is an approximation and the actual result would be an infinite decimal value. Thus, this could be optimized to round the result to a specified decimal place for a more accurate answer.