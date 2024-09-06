```python
def truncate_number(number):
    return number - int(number)
```

The `truncate_number` function takes a positive floating point number as input and returns the decimal part of the number. 

To understand this, imagine we have a beach ball standing on a flat surface. If the ball sticks out over a inch from the surface, we clip the part that's sticking out and only leave the part that's touching the surface. This function performs this clipping by subtracting the largest integer that is less than or equal to a given number (this corresponds to the integer part of the decimal). 

For example, if we apply this operation to 3.5, we get 0.5. This is because 3 is the largest integer that is less than 3.5, so subtracting 3 from 3.5 gives 0.5. 

The function is implemented with a concise one-line syntax that achieves the desired result through simple mathematical operations. It does not require any additional libraries or dependencies.