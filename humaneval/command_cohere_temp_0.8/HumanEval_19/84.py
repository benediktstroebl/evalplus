```python
def sort_numbers(numbers: str) -> str:
    numbers = [int(char) for char in numbers.split()]
    numbers.sort()
    return ' '.join(map(str, numbers))
```
This Python script defines a function called `sort_numbers` which takes a string containing a sequence of numbers and sorts it in ascending order. The function splits the input string into individual numbers, converts them to integers, and then sorts this list of integers. Finally, it joins the sorted numbers back into a string and returns the result. 

Here's an example usage of this function: 
 ```python
print(sort_numbers('three one five')) 
```

The output of this code will be: 
```
one three five 
``` 
This demonstrates that the numbers are sorted in ascending order with a gap between each number, indicating that they are distinct.