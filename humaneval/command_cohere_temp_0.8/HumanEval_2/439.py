```python
def truncate_number(number):
    return number - int(number)
```

The `truncate_number` function takes a positive floating point number as input and returns the decimal part of the number. 

To understand this, imagine we have a beach ball standing on a flat surface. If the ball is slightly tilted towards the right or left, mostly its weight is still supported by the flat surface with a tiny fraction of the ball floating above. If we tilt the ball further, more of it starts floating above the surface and less weight is supported. The `truncate_number` function roughly does the same, it 'tilts' the number until it barely touches an integer (the surface), and the leftover portion is the decimal part which is returned. 

For example, if we input `3.5`, the largest integer smaller is `3` and the leftover float is `0.5`. 

This approach doesn't account for numbers that converge to integers like `3.999999999` which would still return `0.5`. However, it works for the stated use case and is efficient in its simplicity.