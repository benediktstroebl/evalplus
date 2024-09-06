```python
def unique_digits(x):
    odd = [elem for elem in x if not any(int(d) % 2 == 0 for d in str(elem))]
    return sorted(odd)
```

The function `unique_digits` uses a list comprehension that checks each digit in the string representation of an integer to determine if any of its digits are even. After filtering the list, it sorts the values in increasing order and returns them. 

To run the code, you can copy and paste it into a Python interpreter or save it as a `.py` file and execute it using the command line:
```bash
$ python script_name.py
``` 
Ensure you have the appropriate development environment or Python interpreter installed.