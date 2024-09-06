```python
def sum_squares(lst):
    result = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            num **= 2
        elif i % 4 == 0 and i % 3 != 0:
            num **= 3
        result += num
    return result
```
This function sums the elements of the list `lst` element-wise, squared if the index is a multiple of 3, and cubed if the index is a 
multiple of 4 but not a multiple of 3. The sums of the squared and cubed elements are then returned. 

The `enumerate` function is used to iterate through the list with `i` as the index and `num` as the corresponding value. Within the 
loop, the conditions `i % 3 == 0` and `i % 4 == 0 && i % 3 != 0` are used to respectively check if the index is a multiple of 
3 and 4, ensuring the values are squared or cubed accordingly. 

To handle the edge case of an empty list, the function initializes the `result` variable to 0, so that nothing is added to it 
from the empty list. 

This solution can efficiently solve the problem within the specified requirements.