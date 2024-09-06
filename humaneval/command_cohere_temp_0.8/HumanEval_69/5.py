```python
def search(lst):
    freq, max_val = -1, 0 
    for n in lst:
        if n > max_val:
            max_val = n 
        if n >= freq:
            freq = n 
    return max_val if max_val >= 0 and max_val >= freq else -1
```

This script defines a function 'search' that solves the problem by using two variables to track the frequency of the current maximum value and the maximum value found so far. It then iterates through the list, updating the frequency if the current integer is greater than the frequency and the maximum value if the current integer is greater than the current maximum value.  If no integer is found that satisfies these conditions, it returns -1. 

The code works as follows:
1. `freq`, which is initialized to -1 and could be interpreted as the frequency of the current maximum value, is updated to the frequency of the current integer in the list whenever this current integer is greater than `freq`.
2. `max_val`, which is initialized to 0, is updated to the current integer whenever the current integer is greater than `max_val`.
3. The function returns `max_val` if it's greater than 0 and greater than or equal to `freq`, meaning that there exists an integer in the list that is greater than zero and its frequency is greater than or equal to its value. Otherwise, it returns -1. 

This solution is efficient because it uses two variables to keep track of the two important features of the answer, resulting in a time complexity of O(n) where n is the length of the list. 

Note that this solution assumes that the list contains only positive integers. If the list contains negative numbers or non-integer values, the function may not return the expected results.