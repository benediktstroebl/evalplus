```python
def specialFilter(nums):
    oddFirsts = [num for num in nums if int(num[0]) % 2 == 1]
    oddLasts = [num for num in nums if int(num[-1]) % 2 == 1]
    return len(oddFirsts & oddLasts)
```

The script uses Python's array filtering capabilities along with the & operator to find the intersection of the two filtered arrays and then uses `len()` to determine the answer.

To use this script, you can add it to a Python file (e.g., `special_filter.py`) and then run it using the Python interpreter:
```bash
python special_filter.py
``` 

This will execute the script and print the result. 
You can also test this code snippet inside a markdown cell in any Jupiter Notebook by treating each line as an input cell. 

Ensure that the cell is prefixed with three back ticks `` ` `` to enable a code block. 
This will enable you to verify the functionality of the given answer.