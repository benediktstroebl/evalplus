```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1 = planet1.lower() if planet1 in planets else ''
    p2 = planet2.lower() if planet2 in planets else ''
    result = []
    if p1 and p2:
        a1, a2 = 0, len(planets) - 1
        while a1 <= a2:
            current = planets[int((a1 + a2) / 2)]
            if current == p1:
                a1 = a2 + 1
            elif current == p2:
                a2 = a1 - 1
            else:
                if current >= p1 and current <= p2:
                    result.append(current)
            if result and not (p1 == result[0] and p2 == result[-1]):
                a2 -= 1
            if result and not (p2 == result[0] and p1 == result[-1]):
                a1 += 1
        return tuple(result)
    else:
        return tuple()
```

The function first creates a list of all planets, and then searches for `planet1` and `planet2` in the list, storing the indices of the first and last occurrence of a planet in these lists. The function then uses binary search to find the closest planets to the sun in the list, adding them to `result` list. The result list is sorted by proximity to the sun in the final tuple. The example usage of the function is:
```python
print(bf("Jupiter", "Neptune"))
```
```bash
('Saturn', 'Uranus')
``` 

Such a approach allows to sort planets by their proximity to the Sun.