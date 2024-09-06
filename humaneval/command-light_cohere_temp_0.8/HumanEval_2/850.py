```python
def truncate_number(number: float) -> float:
    return 0.1 if number <= 1 else 

# other tests
print(truncate_number(3.0))
print(truncate_number(10.0))
print(truncate_number(-3.0))
print(truncate_number(4.9))
```