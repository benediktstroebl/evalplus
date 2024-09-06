```python
def truncate_number(number):
    return number - int(number)
```
This function simply subtracts the integer part of the number from the original number, this effectively removes the integer part and keeps the decimal part. 

To test this function, here is a sample execution:
```python
trunctate_number(3.5)
# Output: 0.5
```