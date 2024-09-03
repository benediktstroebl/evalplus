Here's the code you requested:
```python
def choose_num(x, y):
    if x > y:
        return x
    if x < y or y < 0:
        return -1
    mid = (x + y) // 2
    if mid % 2 == 0:
        return mid
    return y
```
The function 'choose_num' in this code takes two positive integers 'x' and 'y' as input and determines the biggest even integer in the range [x, y] inclusive. If the input values are out of the range, it returns -1. If there is input is out of the range, it returns -1. If the result is an halfway even number (i.e., the result is even even even, it returns the larger half of the number). If the result is odd, it returns the smaller half of the number.