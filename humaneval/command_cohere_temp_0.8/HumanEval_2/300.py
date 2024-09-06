```python
def truncate_number(number):
    return number - int(number)
```
This function simply subtracts the largest integer less than number, which is achieved by flooring the number, from the original number to leave behind the desired decimal part. 

To test this function, you can call it with a float input like so: 
```python
 truncate_number(3.5)
```
The output will be:
0.5