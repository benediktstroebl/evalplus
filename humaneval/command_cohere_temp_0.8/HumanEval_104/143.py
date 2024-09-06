```python
def unique_digits(x):
    odd = [elem for elem in x if not any(int(d) % 2 == 0 for d in str(elem))]
    return sorted(odd)
```

The function `unique_digits` uses a list comprehension that checks each digit in the string representation of the elements in the list `x`. Elements that don't have any even digits are added to the `odd` list, which is then returned sorted. The tests examples provided in the problem statement are executed successfully. 
For example:
```python
>> unique_digits([15, 33, 1422, 1])
[1, 15, 33]
>> unique_digits([152, 323, 1422, 10])
[]
``` 

This script will work in a Python environment that has markdown support, such as Colab. 
To execute the cell in Colab you need to run the following command: 
```bash
!python
```